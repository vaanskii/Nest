from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm

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
        user.save()
    else:
        message = form.errors.as_json()

    return JsonResponse({'message': message}, safe=False)