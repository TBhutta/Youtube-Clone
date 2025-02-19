from django.db import models
from datetime import datetime

# TODO: Add tags and genre attributes
# TODO: Add help texts, error messages
class Video(models.Model):
    # TODO: Add duration times and comments
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="videos/thumbnails")
    video_file = models.FileField(upload_to="videos/video_files/")
    description = models.TextField()
    upload_date = models.DateTimeField(default=datetime.today().isoformat()) # TODO: Make readonly
    author = models.IntegerField() # TODO: Make readonly
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        db_table = "videos"
    
    def __str__(self):
        return self.title
    
