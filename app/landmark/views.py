from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Landmark
from .serializers import LandmarkSerializer


class LandmarkView(APIView):
    def get(self, request):
        return Response({"message": "za warudo"}, status.HTTP_200_OK)


class LandmarkDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            landmark = Landmark.objects.get(pk=pk)
        except Landmark.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LandmarkSerializer(landmark)
        return Response({"landmark": serializer.data})
