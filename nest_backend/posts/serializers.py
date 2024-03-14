from rest_framework import serializers
from .models import Post, Comments, PostAttachment
from account.serializers import UserSerializer
        
class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'get_image',)

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at', 'likes_count', 'created_at_formatted', 'comments_count', 'attachments')

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = ('id', 'body', 'created_by', 'created_at_formatted', 'comment_likes_count',)

class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at', 'likes_count', 'created_at_formatted', 'comments_count', 'comments', 'attachments')
