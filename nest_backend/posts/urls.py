from django.urls import path
from . import api

urlpatterns = [
    path('', api.posts, name='posts'),
    path('create/', api.create_post, name='create_post'),
    path('get_csrf_token/', api.get_csrf_token, name='get_csrf_token')
]