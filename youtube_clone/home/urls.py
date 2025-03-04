from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("home/", views.home, name="home"),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    path("history/", views.history, name="history"),
    path("playlists/", views.playlists, name="playlists"),
    path("you/", views.library, name="you"),
    path("watch/<int:video_id>/", views.watch_video, name="watch-video"),
    path("watch/<int:video_id>/get-comments/", views.get_comments, name="get-comments"),
    path("watch/<int:video_id>/add-comment/", views.add_comment, name="add-comment"),
]
