from django.db import models
from datetime import datetime

class Video(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="videos/thumbnails")
    video_file = models.FileField(upload_to="videos/video_files/")
    description = models.TextField()
    upload_date = models.DateTimeField(default=datetime.today().isoformat()) # TODO: Make readonly
    author = models.CharField(max_length=100) # TODO: Make readonly
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        db_table = "videos"
