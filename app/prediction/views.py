from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PredictionSerializer


class AddCapture(APIView):
    def post(self, request):
        if "image" not in request.FILES:
            return Response(
                {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        uploaded_file = request.FILES["image"]

        data = {"result": "Kota Lama", "rate": 80, "image": uploaded_file}
        photo_serializer = PredictionSerializer(data=data)

        if photo_serializer.is_valid():
            photo_serializer.save()
            return Response(photo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
