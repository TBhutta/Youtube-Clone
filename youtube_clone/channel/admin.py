from django.contrib import admin
from .models import *

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Playlist)
admin.site.register(Playlist_Video)
admin.site.register(Subscriptions)
admin.site.register(History)
