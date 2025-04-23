from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("filter-videos/", views.filter_videos, name="filter-videos"),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    path("history/", views.history, name="history"),
    path("playlists/", views.playlists, name="playlists"),
    path("you/", views.library, name="you"),
    path("view-channel/<str:channel_username>/", views.view_channel, name="view-channel"),
    path("watch/<int:video_id>/", views.watch_video, name="watch-video"),
    path("watch/<str:video_id>/", views.watch_video, name="watch-video"),
    path("watch/<int:video_id>/get-comments/", views.get_comments, name="get-comments"),
    path("watch/<int:video_id>/add-comment/", views.add_comment, name="add-comment"),
    path("watch/<int:video_id>/like-video/", views.like_video, name="like-video"),
    path("watch/<int:video_id>/dislike-video/", views.dislike_video, name="dislike-video"),
    path("watch/<int:video_id>/increment-views/", views.increment_views, name="increment-views"),
    path("watch/get-recommendations/", views.get_recommendations, name="get-recommendations"),
    path("subscribe/<int:channel_id>/", views.subscribe_to_channel, name="subscribe"),
    path("getting-subscriptions/", views.get_subscriptions, name="get-subscriptions"),
    path("add-video-to-playlist/<int:video_id>/<int:playlist_id>/", views.video_playlist_actions, name="add-video-to-playlist"),
    path("create-playlist/", views.create_playlist, name="create-playlist"),
    path("view-playlist/<int:playlist_id>/", views.view_playlist, name="view-playlist"),
]
