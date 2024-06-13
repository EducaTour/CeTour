import logging
import os
import uuid

from django.conf import settings
from google.cloud import storage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import Model
from .serializers import PredictionSerializer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AddCapture(APIView):
    def post(self, request):
        if "image" not in request.FILES:
            return Response(
                {"message": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        save_directory = "./photo/"

        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        uploaded_file = request.FILES["image"]

        new_filename = f"{uuid.uuid4()}.{uploaded_file.name.split('.')[-1]}"

        file_path = os.path.join(save_directory, new_filename)

        with open(file_path, "wb") as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        try:
            predicted_class_name, confidence_score = Model.predict_class(file_path)

            if float(confidence_score) < 65.0:
                return Response(
                    {
                        "message": "Confidence score below 65%. Please provide a clearer image."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            logger.error(f"Error in prediction: {e}")
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        try:
            client = storage.Client(
                credentials=settings.GS_CREDENTIALS, project=settings.GS_PROJECT_ID
            )
            bucket = client.get_bucket(settings.GS_BUCKET_NAME)
            gcs_destination_path = f"predictions/{predicted_class_name}/{new_filename}"

            blob = bucket.blob(gcs_destination_path)
            blob.upload_from_filename(file_path)
            image_url = blob.public_url
        except Exception as e:
            logger.error(f"Error uploading to GCS: {e}")
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        os.remove(file_path)

        if os.path.exists(file_path) == 0:
            print("File does not exist")

        data = {
            "result": predicted_class_name,
            "rate": confidence_score,
            "image": image_url,
        }
        photo_serializer = PredictionSerializer(data=data)

        if photo_serializer.is_valid():
            photo_serializer.save()
            return Response(photo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Serializer errors: {photo_serializer.errors}")
            return Response(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
