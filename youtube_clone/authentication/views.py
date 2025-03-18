from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import AccountCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from home import views as homeViews
from channel.models import Playlist

USER_MODEL = get_user_model()

def registration(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            if password != confirm_password:
                messages.error(request, "Passwords don't match")
                return redirect(registration)

            f_name = form.cleaned_data["first_name"]
            l_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            profile_pic = form.cleaned_data["profile_pic"]
            about = form.cleaned_data["about"]

            # Creating User entity
            new_user = USER_MODEL.objects.create_user(username, email, password, first_name=f_name, last_name=l_name, about=about, profile_pic=profile_pic)
            new_user.save()

            # Creating 'Likes' playlist for user entity
            new_likes_playlist  = Playlist.objects.create(title="Liked videos", owner=new_user)
            new_likes_playlist.save()

            # Creating 'Dislikes' playlist for user entity
            new_dislikes_playlist  = Playlist.objects.create(title="Disliked videos", owner=new_user)
            new_dislikes_playlist.save()

            return redirect(login_user)

    form = AccountCreationForm()
    return render(request, "authentication/sign-up.html", {
        'form': form
    })

def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(homeViews.library)
            else:
                return redirect(login_user)

    form = UserLoginForm()
    return render(request, "authentication/login.html", {
        "form": form
    })

def logout_user(request):
    logout(request)
    return redirect(homeViews.home)