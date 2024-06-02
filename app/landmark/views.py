from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class LandmarkView(APIView):
    def get(self, request):
        return Response({"message": "hello worldz"}, status.HTTP_200_OK)
