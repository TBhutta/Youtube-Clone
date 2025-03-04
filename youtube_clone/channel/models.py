from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# TODO: Add tags and genre attributes
# TODO: Add help texts, error messages
class Video(models.Model):
    # TODO: Add duration times and comments
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="videos/thumbnails")
    video_file = models.FileField(upload_to="videos/video_files/")
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    author = models.IntegerField() # TODO: Make readonly, make foreign key?
    # FIXME: User model's username is referenced instead of id
    # author = models.ForeignKey(User, on_delete=models.CASCADE) # TODO: look for better on_delete
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        db_table = "videos"
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    replying_to = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "comments"
    
    def __str__(self):
        return self.content
    

# TODO: Add extra stuff to user, e.g. playlists, subscriber count, viewers count, number of videos, comments, likes, subscriptions, notifications, etc
class User_Playlist(models.Model):
    title = models.CharField(max_length=50)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateField(auto_now=True)
    # number of videos will be calculated at runtime as I believe it is not necessary to store that information


# TODO: Add links to user's comments, likes, dislikes, subs, playlists here, or have a look at django's many-to-many
# NOTE: I need this to add file for profile pic
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to="users/profile_pics/")
    about = models.TextField(blank=True)

    def __str__(self):
        return self.user.username