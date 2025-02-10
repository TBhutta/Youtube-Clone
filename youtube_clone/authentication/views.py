from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AccountCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from home import views as homeViews


def registration(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data["first_name"]
            l_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            print(f_name, l_name, username, email, password)
            new_user = User.objects.create_user(username, email, password, first_name=f_name, last_name=l_name)
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
                # return redirect("../../you")
                return redirect(homeViews.library)
            else:
                print("cp")
                return redirect(login_user)

    form = UserLoginForm()
    return render(request, "authentication/login.html", {
        "form": form
    })

def logout_user(request):
    logout(request)
    return redirect(homeViews.home)