from django.urls import path

from .views import LandmarkDetailView, LandmarkView

urlpatterns = [
    path("", LandmarkView.as_view(), name="landmark"),
    path("<int:pk>/", LandmarkDetailView.as_view(), name="landmark-detail"),
]
