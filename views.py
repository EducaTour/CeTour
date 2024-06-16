from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Landmark, LandmarkContent
from .serializers import LandmarkDetailSerializer, LandmarkListSerializer


class LandmarkView(APIView):
    def get(self, request):
        landmarks = Landmark.objects.all()
        serializer = LandmarkListSerializer(landmarks, many=True)
        return Response({"landmarks": serializer.data})


class LandmarkDetailView(APIView):
    def get(self, request, pk):
        try:
            landmark = Landmark.objects.get(pk=pk)
        except Landmark.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LandmarkDetailSerializer(landmark, context={'request': request})
        return Response({"landmark": serializer.data})
