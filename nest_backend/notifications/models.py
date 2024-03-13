from django.db import models
from account.models import User
from posts.models import Post, Comments
import uuid

class Notifications(models.Model):
    STARTFOLLOWING = 'new_following'
    POST_LIKE = 'post_like'
    POST_COMMENT = 'post_comment'
    COMMENT_LIKE = 'comment_like'

    CHOICES_TYPE_OF_NOTIFICATION =(
        (STARTFOLLOWING, 'New following'),
        (POST_LIKE, 'Post like'),
        (POST_COMMENT, 'Post comment'),
        (COMMENT_LIKE, 'Comment like')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    type_of_notification = models.CharField(max_length=50, choices=CHOICES_TYPE_OF_NOTIFICATION)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='created_notification', on_delete=models.CASCADE)
    created_for = models.ForeignKey(User, related_name='received_notification', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
