# Generated by Django 5.0.3 on 2024-03-14 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_liked',
        ),
    ]
