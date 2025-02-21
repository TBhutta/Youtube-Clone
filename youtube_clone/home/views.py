from django.shortcuts import render
from channel.models import Video
from django.contrib.auth.models import User

def home(request):
    recommended_videos = Video.objects.all()
    ids = []
    titles = []
    thumbnails = []
    descriptions = []
    dates = []
    views = []

    for video in recommended_videos:
        ids.append(User.objects.filter(id=video.id))
        titles.append(video.title)
        thumbnails.append(video.thumbnail.url)
        descriptions.append(video.description)
        dates.append(video.upload_date)
        views.append(video.views)

    data = {
        'ids': ids,
        'titles': titles,
        'thumbnails': thumbnails,
        'descriptions': descriptions,
        'dates': dates,
        'views': views
    }

    return render(request, "home/home.html", {
        "recommended_videos": recommended_videos,
        "len": len(recommended_videos)
    })

def subscriptions(request):
    return render(request, "home/subscriptions-page.html", {})

def history(request):
    return render(request, "home/history-page.html", {})

def playlists(request):
    return render(request, "home/playlists-page.html", {})

def library(request):
    return render(request, "home/library.html", {})

