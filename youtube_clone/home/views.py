from django.shortcuts import render
from django.http import JsonResponse
from channel.models import Video, Comment, Playlist, Playlist_Video
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
            "commenter": comment.commenter.username,
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
    # TODO: Ensure only logged in users can like/dislike
    # TODO: Make it so that a user can only like a video once, and if disliked, remove their like

    #TODO: Test this!
    video_in_question = Video.objects.get(id=video_id)
    user_liked_videos_playlist = Playlist.objects.get(title="Liked videos", owner=request.user)
    user_disliked_videos_playlist = Playlist.objects.get(title="Disliked videos", owner=request.user)
    try:
        video_is_liked = Playlist_Video.objects.get(playlist=user_liked_videos_playlist, video=video_in_question)
    except Playlist_Video.DoesNotExist:
        video_is_liked = False
        print("Video does not exist")

    try:
        video_is_disliked = Playlist_Video.objects.get(playlist=user_disliked_videos_playlist, video=video_in_question)
    except Playlist_Video.DoesNotExist:
        video_is_disliked = False
        print("Video does not exist")


    if video_is_liked:
        Playlist_Video.objects.get(playlist=user_liked_videos_playlist, video=video_in_question).delete() # Removing the video from user's "Liked videos playlist"
        video_in_question.likes -= 1 # User is UN-liking (NOT disliking, just removing the like), so decrement likes by 1
        video_in_question.save()

    elif video_is_disliked:
        Playlist_Video.objects.get(playlist=user_disliked_videos_playlist, video=video_in_question).delete()
        video_in_question.dislikes -= 1 # User already has this video disliked, so we need to undo this
        video_in_question.save()

        # Adding video to user's "Liked videos" playlist
        liking_video = Playlist_Video(playlist=user_liked_videos_playlist, video=video_in_question)
        liking_video.save()

        # Incrementing the video in question's likes by 1
        video_in_question.likes += 1
        video_in_question.save()
    else:
        # Adding video to user's "Liked videos" playlist
        liking_video = Playlist_Video(playlist=user_liked_videos_playlist, video=video_in_question)
        liking_video.save()

        # Incrementing the video in question's likes by 1
        video_in_question.likes += 1
        video_in_question.save()

    return JsonResponse({"data": f"successfully liked video {video_id}"})

def dislike_video(request, video_id):
    # TODO: Ensure only logged in users can like/dislike
    # TODO: Make it so that a user can only like a video once, and if disliked, remove their like

    #TODO: Test this!
    video_in_question = Video.objects.get(id=video_id)
    user_liked_videos_playlist = Playlist.objects.get(title="Liked videos", owner=request.user)
    user_disliked_videos_playlist = Playlist.objects.get(title="Disliked videos", owner=request.user)
    try:
        video_is_liked = Playlist_Video.objects.get(playlist=user_liked_videos_playlist, video=video_in_question)
    except Playlist_Video.DoesNotExist:
        video_is_liked = False
        print("Video does not exist")

    try:
        video_is_disliked = Playlist_Video.objects.get(playlist=user_disliked_videos_playlist, video=video_in_question)
    except Playlist_Video.DoesNotExist:
        video_is_disliked = False
        print("Video does not exist")


    if video_is_disliked:
        Playlist_Video.objects.get(playlist=user_disliked_videos_playlist, video=video_in_question).delete() # Removing the video from user's "Disliked videos playlist"
        video_in_question.dislikes -= 1 # User is UN-disliking (NOT liking, just removing the dislike), so decrement dislikes by 1
        video_in_question.save()

    elif video_is_liked:
        Playlist_Video.objects.get(playlist=user_liked_videos_playlist, video=video_in_question).delete()
        video_in_question.likes -= 1 # User already has this video liked, so we need to undo this
        video_in_question.save()

        # Adding video to user's "Disliked videos" playlist
        disliking_video = Playlist_Video(playlist=user_disliked_videos_playlist, video=video_in_question)
        disliking_video.save()

        # Incrementing the video in question's dislikes by 1
        video_in_question.dislikes += 1
        video_in_question.save()
    else:
        # Adding video to user's "Disliked videos" playlist
        disliking_video = Playlist_Video(playlist=user_disliked_videos_playlist, video=video_in_question)
        disliking_video.save()

        # Incrementing the video in question's dislikes by 1
        video_in_question.dislikes += 1
        video_in_question.save()

    return JsonResponse({"data": f"successfully disliked video {video_id}"})

def get_recommendations(request):
    videos = Video.objects.all()
    fetched_videos = {}
    for video in videos:
        fetched_videos[video.id] = {
            "title": video.title,
            "thumbnail": video.thumbnail.url,
            "upload_date": video.upload_date.isoformat(),
            # FIXME: Author is not passed because it's not JSON serializable
            "author": video.author.username,
            "views": video.views,
        }
    return JsonResponse({"videos": json.dumps(fetched_videos)})