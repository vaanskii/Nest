# Generated by Django 5.0.2 on 2024-03-09 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_posts_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posts_count',
        ),
    ]
