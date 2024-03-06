from django.urls import path
from . import api

urlpatterns = [
    path('', api.posts, name='posts'),
    path('create/', api.create_post, name='create_post'),
    path('profile/<uuid:id>/', api.profile_posts, name='profile_posts')
]