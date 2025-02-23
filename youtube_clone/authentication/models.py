from django.db import models
from django.contrib.auth.models import User

# TODO: Add links to user's comments, likes, dislikes, subs, playlists here, or have a look at django's many-to-many
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    # TODO: Add profile pic here

    def __str__(self):
        return self.user.username