# Generated by Django 5.0.3 on 2024-03-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_attachments_postattachment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postattachment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='posts.postattachment'),
        ),
    ]
