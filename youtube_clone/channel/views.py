from django.shortcuts import render, redirect
from .forms import VideoUploadForm, AccountUpdateForm
from authentication.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Video, Playlist, Playlist_Video
from youtube_clone.settings import BASE_DIR

def profile(request):
    return render(request, "channel/profile.html", {})

def update_account(request):
    if request.method == "POST":
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        # TODO: Validate form
        # if form.is_valid():
        form.save()
        print("Account updated")
        return redirect("/")
        # else:
        #     print("form not valid")

    account_update_form = AccountUpdateForm(instance=request.user)
    # user_creation_form = UserCreationForm(instance=request.user)
    return render(request, "channel/update-account.html", {
        # "user_creation_form": user_creation_form,
        "account_update_form": account_update_form
    })

def dashboard(request):
    form = VideoUploadForm()
    user = request.user
    return render(request, "channel/dashboard.html", {
        "form": form,
        "user": user,
    })

def upload_video(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Not committing the form as we still need to set the author's id field
            new_author = form.save(commit=False)
            new_author.author = request.user
            new_author.save()
            messages.success(request, "Video uploaded.")
        else:
            messages.error(request, "Something went wrong.")
    return redirect(dashboard)

def content(request):
    videos = Video.objects.all()

    return render(request, "channel/content.html", {
        "videos": videos
    })

def get_videos(request):
    videos = Video.objects.filter(author = request.user.id)
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
    return JsonResponse(data)

def get_shorts(request):
    # TODO: fetch videos only published by current user
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
    return JsonResponse(data)

def get_live(request):
    return render(request, "channel/content.html", {})

def get_posts(request):
    return render(request, "channel/content.html", {})

def playlists_page(request):
    return render(request, "channel/content.html", {})

def get_podcasts(request):
    return render(request, "channel/content.html", {})

def get_promotions(request):
    return render(request, "channel/content.html", {})

def get_playlists(request, video_id):
    # TODO: Filter out liked and disliked playlist
    fetched_playlists = Playlist.objects.filter(owner=request.user)
    all_playlists = {}
    for playlist in fetched_playlists:
        all_playlists[playlist.id] = playlist.title

    # Below is a list of the user's playlists that already has the video in question saved.
    fetched_playlists = Playlist_Video.objects.filter(playlist__owner=request.user, video=video_id)
    video_saved_playlists = []
    for playlist in fetched_playlists:
        video_saved_playlists.append(playlist.playlist_id)
    return JsonResponse({"playlists": all_playlists, "video_saved_playlists": video_saved_playlists})