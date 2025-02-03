from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def subscriptions(request):
    return render(request, "subscriptions-page.html", {})

def history(request):
    return render(request, "history-page.html", {})