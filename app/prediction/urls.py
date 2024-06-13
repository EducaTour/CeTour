urlpatterns = []
from django.urls import path

from .views import AddCapture

urlpatterns = [
    path("", AddCapture.as_view(), name="landmark"),
]
