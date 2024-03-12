from django.urls import path
from . import api

urlpatterns = [
    path('', api.posts, name='posts'),
    path('create/', api.create_post, name='create_post'),
    path('profile/<uuid:id>/', api.profile_posts, name='profile_posts'),
    path('<uuid:pk>/', api.post_detail, name='post_detail'),
    path('<uuid:id>/delete/', api.delete_post, name='delete_post'),
    path('<uuid:id>/like/', api.like_post, name='like_post'),
    path('<uuid:id>/comment/', api.create_comment, name='create_comment'),
    path('<uuid:id>/delete-comment/', api.delete_comment, name='delete_comment'),
    path('<uuid:id>/like-comment/', api.like_comment, name='like_comment')
]