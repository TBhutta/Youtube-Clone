from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.registration, name="sign-up"),
    path("sign-in/", views.login_user, name="sign-in"),
    path("logout/", views.logout_user, name="logout"),
]
