import uuid
from django.db import models
from account.models import User
from django.utils.timezone import now


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='comments_like', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(blank=True, null=True, max_length=2000)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    comment_likes = models.ManyToManyField(CommentLike, blank=True)
    comment_likes_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at',]

    def created_at_formatted(self):
        time_difference = now() - self.created_at
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes = remainder // 60

        if days > 0:
            return f"{days}d"
        elif hours > 0:
            return f"{hours}h"
        else:
            return f"{minutes}m"
        
    def __str__(self):
        max_chars = 30
        if len(self.body) > max_chars:
            return f"{self.body[:max_chars]}..."
        return self.body


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(blank=True, null=True, max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    likes = models.ManyToManyField(Like, blank=True)
    likes_count = models.IntegerField(default=0)

    comments = models.ManyToManyField(Comments, blank=True)
    comments_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.body:
            return
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def created_at_formatted(self):
        time_difference = now() - self.created_at
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes = remainder // 60

        if days > 0:
            return f"{days}d"
        elif hours > 0:
            return f"{hours}h"
        else:
            return f"{minutes}m"




    def __str__(self):
        return self.body
