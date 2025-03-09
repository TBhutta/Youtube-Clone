from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# TODO: Add links to user's comments, likes, dislikes, subs, playlists here, or have a look at django's many-to-many
class Account(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to="users/profile_pics/", null=True, blank=True)
    about = models.TextField(blank=True)

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