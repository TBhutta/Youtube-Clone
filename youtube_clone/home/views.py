from django.shortcuts import render
from channel.models import Video
from django.contrib.auth.models import User

def home(request):
    recommended_videos = Video.objects.all()
    for i in recommended_videos:
        print(i.author)
    
    # ids = []
    # titles = []
    # thumbnails = []
    # descriptions = []
    # dates = []
    # views = []

    # for video in recommended_videos:
    #     ids.append(User.objects.filter(id=video.id))
    #     titles.append(video.title)
    #     thumbnails.append(video.thumbnail.url)
    #     descriptions.append(video.description)
    #     dates.append(video.upload_date)
    #     views.append(video.views)

    # data = {
    #     'ids': ids,
    #     'titles': titles,
    #     'thumbnails': thumbnails,
    #     'descriptions': descriptions,
    #     'dates': dates,
    #     'views': views
    # }

    return render(request, "home/home.html", {
        "recommended_videos": recommended_videos,
    })

def subscriptions(request):
    return render(request, "home/subscriptions-page.html", {})

def history(request):
    return render(request, "home/history-page.html", {})

def playlists(request):
    return render(request, "home/playlists-page.html", {})

def library(request):
    return render(request, "home/library.html", {})

def watch_video(request, video_id=None):
    # FIXME: Pass in id of actual selected video so that can be displayed
    if video_id:
        selected_video = Video.objects.filter(id=video_id).first()
    else:
        selected_video = Video.objects.filter(id=9).first()
    # print(selected_video.title)
    author = User.objects.filter(id=selected_video.author).first()
    # print(author.username)
    return render(request, "home/watch-video.html", {
        "selected_video": selected_video,
        "channel_username": author.username,
    })

def test(request, id):
    print("hello worls ", id)

    return render(request, "home/home.html", {})