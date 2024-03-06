from rest_framework import serializers

from .models import User, FollowSystem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile_number', 'following', 'followers', 'followers_count', 'following_count', 'posts_count',)

class FollowSystemSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FollowSystem
        fields = ('id', 'followed_by', 'followed_for',)
