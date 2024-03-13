from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from notifications.utils import create_notification

from PIL import Image

from .models import User, FollowSystem
from .serializers import UserSerializer
from .forms import SignupForm, ProfileForm

@api_view(['GET'])
def user(request):
    if hasattr(request.user, 'mobile_number'):
        mobile_number = str(request.user.mobile_number)
    else:
        mobile_number = None

    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'mobile_number': mobile_number,
        'profile_picture': request.user.get_profile_picture()
    })

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'username': data.get('username'),
        'mobile_number': data.get('mobile_number'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        user = form.save()
        user.is_active = False
        user.save()

        url = f'{settings.WEBSITE_URL}/activateEmail/?email={user.email}&id={user.id}'

        send_mail(
            "Please verify your email",
            f"The url for activating your account is: {url}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    else:
        message = form.errors.as_json()

    return JsonResponse({'message': message}, safe=False)

@api_view(['GET'])
@login_required
def profileview(request, id):
    user = User.objects.get(pk=id)
    user_serializer = UserSerializer(user)

    is_following = request.user.is_authenticated and request.user.following.filter(id=id).exists()

    return JsonResponse({
        'user': user_serializer.data,
        'is_following': is_following,
    }, safe=False)

@api_view(['POST'])
def editprofile(request):
    user = request.user
    email = request.data.get('email') 
    username = request.data.get('username')
    mobile_number = request.data.get('mobile_number')

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({'message': 'Email already exists'})
    elif User.objects.exclude(id=user.id).filter(username=username).exists():
        return JsonResponse({'message': 'Username already exists'})
    elif User.objects.exclude(id=user.id).filter(mobile_number=mobile_number).exists():
        return JsonResponse({'message': 'Mobile number already exists'})
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            if 'profile_picture' in request.FILES:
                # Retrieve the uploaded image file
                image_file = request.FILES['profile_picture']

                img = Image.open(image_file)
                
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                img.save(user.profile_picture.path, format='JPEG')

            form.save()

            serializer = UserSerializer(user)

            return JsonResponse({
                'message': 'Information updated',
                'user': serializer.data
            }, safe=False)
        else:
            return JsonResponse({'message': 'Form data is not valid'})


@api_view(['GET'])
def following(request, id):
    user = User.objects.get(id=id)
    following = user.following.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'following': UserSerializer(following, many=True).data,
    }, safe=False)

@api_view(['GET'])
def followers(request, id):
    user = User.objects.get(id=id)
    followers = user.followers.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'followers': UserSerializer(followers, many=True).data,
    }, safe=False)

@api_view(['POST'])
def follow_user(request, id):
    user_to_follow = get_object_or_404(User, id=id)

    if user_to_follow == request.user:
        return JsonResponse({'message': 'You cannot follow yourself!'}, status=400)

    if not request.user.following.filter(id=id).exists():
        following = FollowSystem.objects.create(follower=request.user, following=user_to_follow)
        print(f"Follow relationship created: {request.user.username} -> {user_to_follow.username}")

        request.user.following.add(user_to_follow)
        user_to_follow.followers.add(request.user)

        request.user.following_count = request.user.following.count()
        user_to_follow.followers_count = user_to_follow.followers.count()

        request.user.save()
        user_to_follow.save()

        notification = create_notification(request, 'new_following', following_id=following.id)


    return JsonResponse({'message': f'Now following {user_to_follow.username}'}, safe=False)




@api_view(['POST'])
def unfollow_user(request, id):
    user_to_unfollow = get_object_or_404(User, id=id)
    
    if user_to_unfollow == request.user:
        return JsonResponse({'message': 'You cannot unfollow yourself!'}, status=400)

    request.user.following.remove(user_to_unfollow)
    user_to_unfollow.followers.remove(request.user)
    
    request.user.following_count = request.user.following.count()
    user_to_unfollow.followers_count = user_to_unfollow.followers.count()

    request.user.save()
    user_to_unfollow.save()

    return JsonResponse({'message': f'Unfollowed {user_to_unfollow.username}'}, safe=False)