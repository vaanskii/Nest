from django.http import JsonResponse
from django.middleware import csrf
from rest_framework.decorators import api_view

from .models import Post
from account.models import User
from account.serializers import UserSerializer
from .forms import PostForm
from .serializers import PostSerializer

def get_csrf_token(request):
    token = csrf.get_token(request)
    return JsonResponse({'CSRFtoken': token})


@api_view(['GET'])
def posts(request):
    user_ids = [request.user.id]

    for follower in request.user.following.all():
        user_ids.append(follower.id)

    user_ids.append(request.user.id)

    posts = Post.objects.filter(created_by_id__in=user_ids)
    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def profile_posts(request, id):
    user = User.objects.get(id=id)
    posts = Post.objects.filter(created_by_id=id)

    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse({
        'posts': posts_serializer.data,
        'user': user_serializer.data
    }, safe=False)


@api_view(['POST'])
def create_post(request):
    form = PostForm(request.POST)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        user = request.user
        user.posts_count += 1
        user.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add something here later!...'})