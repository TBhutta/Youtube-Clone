from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# TODO: Add tags and genre attributes
# TODO: Add help texts, error messages
class Video(models.Model):
    # TODO: Add duration times and comments
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="videos/thumbnails")
    video_file = models.FileField(upload_to="videos/video_files/")
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    # author = models.IntegerField() # TODO: Make readonly, make foreign key?
    # FIXME: User model's username is referenced instead of id
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # TODO: look for better on_delete
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
    date_time = models.DateTimeField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    replying_to = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "comments"
    
    def __str__(self):
        return self.content
    

# TODO: Add extra stuff to user, e.g. playlists, subscriber count, viewers count, number of videos, comments, likes, subscriptions, notifications, etc
