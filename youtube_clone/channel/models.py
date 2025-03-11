from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


# TODO: Add tags and genre attributes
# TODO: Add help texts, error messages
class Video(models.Model):
    # TODO: Add duration times and comments
    title = models.CharField(max_length=100, null=False, blank=False)
    thumbnail = models.ImageField(upload_to="videos/thumbnails")
    video_file = models.FileField(upload_to="videos/video_files/", null=False, blank=False)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, null=False, blank=False) # TODO: look for better on_delete
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        db_table = "videos"
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    commenter = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
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
class Playlist(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    # number of videos will be calculated at runtime as I believe it is not necessary to store that information

    class Meta:
        db_table = "playlists"


class Playlist_Video(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        db_table = "playlist_videos"
