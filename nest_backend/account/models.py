import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, mobile_number, **extra_fields):
        if not username:
            raise ValueError("You have not provided a valid username")
    
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=self.normalize_email(email), mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, username=None, email=None, password=None, mobile_number=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, mobile_number, **extra_fields)
    
    def create_superuser(self, username=None, email=None, password=None, mobile_number=None, **extra_fields):
        if mobile_number is None:
            mobile_number = '' 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, mobile_number, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    mobile_number = PhoneNumberField(blank=False, null=False, unique=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    posts_count = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


class FollowSystem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    follower = models.ForeignKey(User, related_name='follower_follows', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='received_follow', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)