from django.shortcuts import render

def dashboard(request, user):
    return render(request, "channel/dashboard.html", {})