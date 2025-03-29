from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Account(AbstractUser):
    profile_pic = models.ImageField(upload_to="users/profile_pics/", null=True, blank=True)
    about = models.TextField(blank=True)
    subscribers = models.IntegerField(default=0)
    # TODO: Add code to automatically increment/ decrement number of videos
    number_of_videos = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        Group,
        related_name="account_users",  # Change related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="account_users_permissions",  # Change related_name
        blank=True
    )
