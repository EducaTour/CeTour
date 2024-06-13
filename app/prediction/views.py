from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from google.cloud import storage
from django.conf import settings
import os
import logging
import uuid

from .serializers import PredictionSerializer
from . import Model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AddCapture(APIView):
    def post(self, request):
        if "image" not in request.FILES:
            return Response(
                {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )
    
        # Specify the directory where you want to save the file
        save_directory = "/photo/"  # Change this to your desired directory
        
        # Make sure the directory exists, create if it doesn't
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        # Get the file data
        uploaded_file = request.FILES["image"]

        new_filename = f"{uuid.uuid4()}.{uploaded_file.name.split('.')[-1]}"

        # Create a file path to save the uploaded file
        file_path = os.path.join(save_directory, new_filename)
        
        # Write the content of the uploaded file to the new file
        with open(file_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        try:
            # Preprocess the image and predict the class
            predicted_class_name, confidence_score = Model.predict_class(file_path)

            # Check if confidence score is below 65%
            if float(confidence_score) < 65.0:
                # Return JSON response with bad request status and message
                return Response({"error": "Confidence score below 65%. Please provide a clearer image."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error in prediction: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Upload the image to Google Cloud Storage and get the URL
        try:
            client = storage.Client(credentials=settings.GS_CREDENTIALS, project=settings.GS_PROJECT_ID)
            bucket = client.get_bucket(settings.GS_BUCKET_NAME)
            # Construct the destination path in GCS
            gcs_destination_path = f"predictions/{predicted_class_name}/{new_filename}"
            
            # Upload the file to GCS with the constructed destination path
            blob = bucket.blob(gcs_destination_path)
            blob.upload_from_filename(file_path)
            image_url = blob.public_url
        except Exception as e:
            logger.error(f"Error uploading to GCS: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        os.remove(file_path)
        
        # Verify file existence before removal
        if os.path.exists(file_path) == 0:
            print("File does not exist")
        
        # Create data dictionary for serializer
        data = {"result": predicted_class_name, "rate": confidence_score, "image": image_url}
        photo_serializer = PredictionSerializer(data=data)

        if photo_serializer.is_valid():
            photo_serializer.save()
            return Response(photo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Serializer errors: {photo_serializer.errors}")
            return Response(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
