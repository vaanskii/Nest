import uuid
from django.db import models
from account.models import User
from django.utils.timezone import now


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(blank=True, null=True, max_length=256)

    likes = models.ManyToManyField(Like, blank=True)
    likes_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

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
            return f"{days} {'day' if days == 1 else 'days'} and {hours} {'hour' if hours == 1 else 'hours'} ago"
        elif hours > 0:
            return f"{hours} {'hour' if hours == 1 else 'hours'} and {minutes} {'minute' if minutes == 1 else 'minutes'} ago"
        else:
            return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"


    def __str__(self):
        return self.body
    

