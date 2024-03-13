from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('user/', api.user, name='user'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/<uuid:id>/', api.profileview, name='profileview'),
    path('following/<uuid:id>/follow/', api.follow_user, name='follow_user'),
    path('following/<uuid:id>/unfollow/', api.unfollow_user, name='unfollow_user'),
    path('following/<uuid:id>/', api.following, name='following'),
    path('followers/<uuid:id>/', api.followers, name='followers'),
    path('editprofile/', api.editprofile, name='edit_profile')
]