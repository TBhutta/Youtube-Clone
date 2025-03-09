from django.contrib import admin
from .models import Video, Comment, User_Playlist

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(User_Playlist)
