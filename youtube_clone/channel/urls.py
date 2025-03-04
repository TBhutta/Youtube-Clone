from django.urls import path
from . import views

urlpatterns = [
    # path("dashboard/<int:user_id>/", views.dashboard, name="dashboard"), # FIXME: figure out how to add account id in url
    path("", views.profile, name="profile"),
    path("update-account/", views.update_account, name="update-account"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/upload-video/", views.upload_video, name="upload-video"),
    path("content", views.content, name="content"),
    path("content/videos", views.get_videos, name="content-videos"),
    path("content/shorts", views.get_shorts, name="content-shorts"),
    path("content/live", views.get_live, name="content-live"),
    path("content/posts", views.get_posts, name="content-posts"),
    path("content/playlists", views.get_playlists, name="content-playlists"),
    path("content/podcasts", views.get_podcasts, name="content-podcasts"),
    path("content/promotions", views.get_promotions, name="content-promotions"),
]
