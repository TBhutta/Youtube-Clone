from datetime import datetime

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from channel.models import Video, Comment, Playlist, Playlist_Video, Subscriptions, History
from django.contrib.auth import get_user_model
import json


USER_MODEL = get_user_model()


def home(request):
    subscriptions = Subscriptions.objects.filter(subscriber=request.user)
    return render(request, "home/home.html", {
        "subscriptions": subscriptions,
    })

def filter_videos(request):
    data = json.loads(request.body)
    if data["filter"] == "all":
        videos = Video.objects.all().values("id", "title", "description", "thumbnail", "upload_date", "author__username", "author__profile_pic", "views")

        # Convert image paths to full URLs
        for video in videos:
            video["thumbnail"] = f"{settings.MEDIA_URL}{video['thumbnail']}"
            video["author__profile_pic"] = f"{settings.MEDIA_URL}{video['author__profile_pic']}"

    else:
        videos = []
    return JsonResponse(list(videos), safe=False)
    # return JsonResponse({"videos": json.dumps(fetched_videos)})

def subscribe_to_channel(request, channel_id):
    channel_to_subscribe = USER_MODEL.objects.get(id=channel_id)
    new_subscription = Subscriptions(subscriber=request.user, subscribing_to=channel_to_subscribe)
    new_subscription.save()
    channel_to_subscribe.subscribers += 1
    channel_to_subscribe.save()
    return JsonResponse({"status": "subscribed"})

def subscriptions(request):
    return render(request, "home/subscriptions-page.html", {})

def get_subscriptions(request):
    # TODO: Make this run on every publicly available page
    subscriptions = {}
    for channel in Subscriptions.objects.filter(subscriber=request.user):
        subscriptions[channel.id] = {
            "username": channel.subscribing_to.username,
            "profile_pic": channel.subscribing_to.profile_pic.url,
        }
    return JsonResponse({"subscriptions": json.dumps(subscriptions)})

def get_history(request):
    history_records = History.objects.filter(user=request.user)
    videos = []
    for record in history_records:
        videos.append(record.video)
    videos = reversed(videos)
    return render(request, "home/history-page.html", {
        "videos": videos
    })

def add_video_to_history(request, video_id):
    if request.user.is_authenticated:
        video = Video.objects.get(id=video_id)
        new_history = History(video=video, user=request.user)
        new_history.save()

def playlists(request):
    return render(request, "home/playlists-page.html", {})

def library(request):
    return render(request, "home/library.html", {})

def watch_video(request, video_id=None):
    add_video_to_history(request, video_id)
    selected_video = Video.objects.filter(id=video_id).first()
    video_age = datetime.now().timestamp() - selected_video.upload_date.timestamp()
    try:
        is_subscribed = Subscriptions.objects.get(subscriber=request.user, subscribing_to=selected_video.author)
        is_subscribed = True
    except:
        is_subscribed = False

    return render(request, "home/watch-video.html", {
        "selected_video": selected_video,
        "profile_pic": request.user.profile_pic.url,
        "is_subscribed": is_subscribed,
    })

def get_comments(request, video_id):
    # TODO: Re-arrange the fetched comments to display the user's comments (if any) at the top.
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
            "commenter_profile_pic": comment.commenter.profile_pic.url,
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

def increment_views(request, video_id):
    video_in_question = Video.objects.get(id=video_id)
    video_in_question.views += 1
    video_in_question.save()
    return JsonResponse({"data": f"successfully incremented views for {video_id}"})

def get_recommendations(request):
    videos = Video.objects.all()
    fetched_videos = {}
    for video in videos:
        fetched_videos[video.id] = {
            "title": video.title,
            "thumbnail": video.thumbnail.url,
            "upload_date": video.upload_date.isoformat(),
            "author": video.author.username,
            "views": video.views,
        }
    return JsonResponse({"videos": json.dumps(fetched_videos)})

def view_channel(request, channel_username):
    channel_to_view = USER_MODEL.objects.get(username=channel_username)
    return render(request, "home/view-channel.html", {
        "channel": channel_to_view,
    })

def video_playlist_actions(request, video_id, playlist_id):
    data = json.loads(request.body)
    if data['action'] == 'checked':
        add_video_to_playlist = Playlist_Video(playlist_id=playlist_id, video_id=video_id)
        add_video_to_playlist.save()
        return JsonResponse({"data": f"successfully added video {video_id} to playlist {playlist_id}"})
    elif data['action'] == 'unchecked':
        remove_video_from_playlist = Playlist_Video.objects.get(playlist_id=playlist_id, video_id=video_id)
        remove_video_from_playlist.delete()
        return JsonResponse({"data": f"successfully removed video {video_id} from playlist {playlist_id}"})


