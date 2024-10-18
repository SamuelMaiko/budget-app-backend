from a_authentication.managers import CustomUserManager
from a_shared.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    username=models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_joined=models.DateTimeField(default=timezone.now)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    # is_verified=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()
    
    class Meta:
        db_table = "users"
        ordering = ("-created_at",)