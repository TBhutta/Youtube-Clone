from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import AccountCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from home import views as homeViews

USER_MODEL = get_user_model()

def registration(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST, request.FILES)
        if form.is_valid():
            f_name = form.cleaned_data["first_name"]
            l_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            profile_pic = form.cleaned_data["profile_pic"]
            about = form.cleaned_data["about"]
            # print(f_name, l_name, username, email, password, profile_pic)
            new_user = USER_MODEL.objects.create_user(username, email, password, first_name=f_name, last_name=l_name, about=about, profile_pic=profile_pic)
            new_user.save()
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