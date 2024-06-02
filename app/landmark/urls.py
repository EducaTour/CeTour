from django.urls import path

from .views import LandmarkView

urlpatterns = [
    path("", LandmarkView.as_view(), name="landmark"),
]
