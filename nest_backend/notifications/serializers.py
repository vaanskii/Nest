from rest_framework import serializers


from .models import Notifications


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('id', 'body', 'type_of_notification', 'post_id', 'created_for_id', 'comment_id', 'created_by')