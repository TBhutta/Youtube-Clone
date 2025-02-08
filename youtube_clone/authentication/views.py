from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import AccountCreationForm

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

    form = AccountCreationForm()
    return render(request, "authentication/sign-up.html", {
        'form': form
    })

def login_user(request):
    return render(request, "authentication/login.html", {})