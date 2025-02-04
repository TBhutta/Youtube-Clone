from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.registration, name="sign-up"),
]
