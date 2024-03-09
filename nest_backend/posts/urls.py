from django.urls import path
from . import api

urlpatterns = [
    path('', api.posts, name='posts'),
    path('create/', api.create_post, name='create_post'),
    path('profile/<uuid:id>/', api.profile_posts, name='profile_posts'),
    path('<uuid:pk>/', api.post_detail, name='post_detail'),
    path('<uuid:id>/delete/', api.delete_post, name='delete_post')
]