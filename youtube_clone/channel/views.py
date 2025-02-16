from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from django.contrib import messages
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