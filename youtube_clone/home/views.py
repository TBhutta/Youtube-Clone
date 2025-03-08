from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from channel.models import Video, Comment
from django.contrib.auth.models import User
import json

def home(request):
    recommended_videos = Video.objects.all()
    # TODO: Acquire channel username from author id of all recommended videos
    
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
    selected_video = Video.objects.filter(id=video_id).first()
    author = User.objects.filter(id=selected_video.author).first()
    return render(request, "home/watch-video.html", {
        "selected_video": selected_video,
        "channel_username": author.username,
    })

def get_comments(request, video_id):
    fetched_comments = Comment.objects.filter(video_id=video_id).all()
    all_comments = {}
    # FIXME: Newly added comment is not fetched right after posting commenting
    for comment in fetched_comments:
        all_comments[comment.id] = {
            "content": comment.content,
            "likes": comment.likes,
            "dislikes": comment.dislikes,
            "date_posted": comment.date_time.isoformat(),
            "commenter": User.objects.get(id=comment.commenter_id).username,
        }
    return JsonResponse({"comments": json.dumps(all_comments)})

def add_comment(request, video_id):
    data = json.loads(request.body)
    video = Video.objects.get(id=video_id)
    new_comment = Comment(commenter=request.user,
                          content=data["new_comment"],
                          video_id=video,
                          )
    new_comment.save()
    return JsonResponse({"data": f"hello word {video_id}"})

def like_video(request, video_id):
    # TODO: Make it so that a user can only like a video once, and if disliked, remove their like
    video = Video.objects.get(id=video_id)
    video.likes += 1
    video.save()
    return JsonResponse({"data": f"successfully liked video {video_id}"})

def get_recommendations(request):
    videos = Video.objects.all()
    fetched_videos = {}
    for video in videos:
        fetched_videos[video.id] = {
            "title": video.title,
            "thumbnail": video.thumbnail.url,
            "upload_date": video.upload_date.isoformat(),
            "author": video.author,
            "views": video.views,
        }
    return JsonResponse({"videos": json.dumps(fetched_videos)})