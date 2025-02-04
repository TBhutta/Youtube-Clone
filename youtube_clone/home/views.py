from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def subscriptions(request):
    return render(request, "subscriptions-page.html", {})

def history(request):
    return render(request, "history-page.html", {})

def playlists(request):
    return render(request, "playlists-page.html", {})