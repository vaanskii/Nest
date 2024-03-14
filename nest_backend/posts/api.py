from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Post, Comments, Like, CommentLike
from account.models import User
from account.serializers import UserSerializer
from .forms import PostForm, AttachmentForm
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from notifications.utils import create_notification
from django.db.models import Q
from django.db.models import F


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
def post_detail(request, pk):
    user_ids = [request.user.id]

    for follower in request.user.following.all():
        user_ids.append(follower.id)

    post = Post.objects.filter(Q(created_by_id__in=list(user_ids))).get(pk=pk)

    return JsonResponse({
        'post': PostDetailSerializer(post).data
    })

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
    attachment = None
    attachment_form = AttachmentForm(request.POST, request.FILES)

    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        if attachment:
            post.attachments.add(attachment)

        user = request.user
        user.posts_count += 1
        user.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add something here later!...'})
    
    
@api_view(['DELETE'])
def delete_post(request, id):
    try:
        post = Post.objects.get(created_by=request.user, id=id)
        post.delete()

        user = request.user
        user.posts_count -= 1
        user.save()

        return JsonResponse({'message': 'Deleted'})
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_comment(request, id):
    comment = Comments.objects.create(body=request.data.get('body'), created_by=request.user)

    post = Post.objects.get(id=id)
    post.comments.add(comment)
    post.comments_count += 1
    post.save()

    notification = create_notification(request, 'post_comment', post_id=post.id)

    serializer = CommentSerializer(comment)

    return JsonResponse(serializer.data, safe=False)

@api_view(['DELETE'])
def delete_comment(request, id):
    try:
        comment = Comments.objects.get(created_by=request.user, id=id)
        post = Post.objects.filter(comments=comment).first()

        if post:
            post.comments_count = F('comments_count') - 1
            post.save()

        comment.delete()

        return JsonResponse({'message': 'Comment Deleted'})
    except Comments.DoesNotExist:
        return JsonResponse({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    user = request.user

    if not post.likes.filter(created_by=user).exists():
        like = Like.objects.create(created_by=user)
        post.likes.add(like)
        post.likes_count += 1
        post.save()

        notification = create_notification(request, 'post_like', post_id=post.id)

        return JsonResponse({'message': 'Liked'})
    else:
        like = post.likes.filter(created_by=user).first()

        if like:
            like.delete()
            post.likes_count -= 1
            post.save()

            return JsonResponse({'message': 'Unliked'})
        else:
            return JsonResponse({'message': 'Error: Like not found'}, status=400)
        
@api_view(['POST'])
def like_comment(request, id):
    comment = get_object_or_404(Comments, id=id)
    user = request.user

    if not comment.comment_likes.filter(created_by=user).exists():
        like = CommentLike.objects.create(created_by=user)
        comment.comment_likes.add(like)
        comment.comment_likes_count += 1
        comment.save()

        notification = create_notification(request, 'comment_like', comment_id=comment.id)

        return JsonResponse({'message': 'Liked'})
    else:
        like = comment.comment_likes.filter(created_by=user).first()

        if like:
            like.delete()
            comment.comment_likes_count -= 1
            comment.save()
            
            return JsonResponse({'message': 'Unliked'})
        else:
            return JsonResponse({'message': 'error: Like not found'}, status=400)