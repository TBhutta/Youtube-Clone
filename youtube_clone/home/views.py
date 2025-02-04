from django.shortcuts import render

def home(request):
    return render(request, "home/home.html", {})

def subscriptions(request):
    return render(request, "home/subscriptions-page.html", {})

def history(request):
    return render(request, "home/history-page.html", {})

def playlists(request):
    return render(request, "home/playlists-page.html", {})