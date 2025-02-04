from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    path("history/", views.history, name="history"),
    path("playlists/", views.playlists, name="playlists"),
]
