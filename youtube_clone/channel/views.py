from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Video
from youtube_clone.settings import BASE_DIR
import PIL

def dashboard(request):
    form = VideoUploadForm()
    return render(request, "channel/dashboard.html", {
        "form": form
    })

def upload_video(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.author = request.user.id
            new_author.save()
            messages.success(request, "Video uploaded.")
        else:
            messages.error(request, "Something went wrong.")
    return redirect(dashboard)

def content(request):
    return render(request, "channel/content.html", {})

def get_videos(request):
    data = {
        "name": "My Name Is Jeff"
    }
    return JsonResponse(data)

def get_shorts(request):
    videos = Video.objects.all()
    titles = []
    thumbnails = []
    descriptions = []
    dates = []
    views = []
    likes = []
    dislikes = []
    
    for video in videos:
        titles.append(video.title)
        thumbnails.append(video.thumbnail.url)
        descriptions.append(video.description)
        dates.append(video.upload_date)
        views.append(video.views)
        likes.append(video.likes)
        dislikes.append(video.dislikes)
    
    base_dir = str(BASE_DIR)

    data = {
        "titles": titles,
        "thumbnails": thumbnails,
        "descriptions": descriptions,
        "dates": dates,
        "views": views,
        "likes": likes,
        "dislikes": dislikes,
        "base_dir": base_dir,
    }
    print(thumbnails)
    print(base_dir)
    print("/Users/talhah/Documents/python-projects/Youtube-Clone/youtube_clone/media/videos/thumbnails/apple_watch_series_9_0Qg6lz3.jpg")
    return JsonResponse(data)

def get_live(request):
    return render(request, "channel/content.html", {})

def get_posts(request):
    return render(request, "channel/content.html", {})

def get_playlists(request):
    return render(request, "channel/content.html", {})

def get_podcasts(request):
    return render(request, "channel/content.html", {})

def get_promotions(request):
    return render(request, "channel/content.html", {})

