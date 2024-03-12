from rest_framework import serializers
from .models import Post, Comments
from account.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at', 'likes_count', 'created_at_formatted', 'comments_count')
        
class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = ('id', 'body', 'created_by', 'created_at_formatted', 'comment_likes_count',)

class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at', 'likes_count', 'created_at_formatted', 'comments_count', 'comments')
