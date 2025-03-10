from django.shortcuts import render
from django.http import JsonResponse
from channel.models import Video, Comment
from django.contrib.auth import get_user_model
import json

USER_MODEL = get_user_model()

def home(request):
    recommended_videos = Video.objects.all()

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
    return render(request, "home/watch-video.html", {
        "selected_video": selected_video,
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
            "commenter": USER_MODEL.objects.get(id=comment.commenter_id).username,
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
            # FIXME: Author is not passed because it's not JSON serializable
            "author": json.dumps(video.author),
            "views": video.views,
        }
        print(json.dumps(video.author))
    return JsonResponse({"videos": json.dumps(fetched_videos)})