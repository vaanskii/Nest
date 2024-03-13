from .models import Notifications

from posts.models import Post, Comments
from account.models import FollowSystem

def create_notification(request, type_of_notification, post_id=None, comment_id=None, following_id=None):
    created_for = None

    if type_of_notification == 'post_like':
        post = Post.objects.get(pk=post_id)
        if post.created_by != request.user:
            created_for = post.created_by
            body = f'{request.user.username} liked one of your posts!'
        else:
            return None
    elif type_of_notification == 'comment_like':
        comment = Comments.objects.get(pk=comment_id)
        if comment.created_by != request.user:
            created_for = comment.created_by
            body = f'{request.user.username} liked one of your comments!'
        else:
            return None
    elif type_of_notification == 'new_following':
        following = FollowSystem.objects.get(pk=following_id)
        created_for = following.following
        body = f'{request.user.username} started following you!'
    elif type_of_notification == 'post_comment':
        post = Post.objects.get(pk=post_id)
        created_for = post.created_by
        body = f'{request.user.username} commented on your post.'

    # Check if the user is not creating a notification for themselves
    if created_for and created_for != request.user:
        # Create a new notification for every comment
        notification = Notifications.objects.create(
            body=body,
            type_of_notification=type_of_notification,
            created_by=request.user,
            post_id=post_id,
            created_for=created_for,
            comment_id=comment_id
        )
        return notification

    return None
