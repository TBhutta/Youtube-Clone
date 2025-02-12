from django.urls import path
from . import views

urlpatterns = [
    # path("dashboard/<int:user_id>/", views.dashboard, name="dashboard"), # FIXME: figure out how to add account id in url
    path("dashboard/", views.dashboard, name="dashboard"),
]
