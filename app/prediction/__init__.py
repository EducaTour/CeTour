import logging
import tempfile

from django.conf import settings
from google.cloud import storage

from .prediction import Prediction

LABELS = sorted(
    [
        "benteng_vredeburg",
        "candi_borobudur",
        "candi_prambanan",
        "garuda_wisnu_kencana",
        "gedung_sate",
        "istana_maimun",
        "jam_gadang",
        "keong_mas",
        "keraton_jogja",
        "kota_tua",
        "lawang_sewu",
        "masjid_istiqlal",
        "masjid_menara_kudus",
        "masjid_raya_baiturrahman",
        "menara_siger_lampung",
        "monas",
        "monumen_bandung_lautan_api",
        "monumen_gong_perdamaian",
        "monumen_nol_km",
        "monumen_simpang_lima_gumul",
        "patung_ikan_surabaya",
        "patung_yesus_memberkati",
        "tugu_jogja",
        "tugu_khatulistiwa",
        "tugu_pahlawan_surabaya",
    ]
)

# # Initialize the model
# Model = Prediction(
#     model_path="./prediction/model_predic/best_model_2.h5",
#     target_size=(224, 224),
#     classes=LABELS)

try:
    client = storage.Client(
        credentials=settings.GS_CREDENTIALS, project=settings.GS_PROJECT_ID
    )
    bucket = client.get_bucket(settings.GS_BUCKET_NAME)
    # Construct the source path in GCS
    gcs_source_path = "model/best_model_2.h5"

    # Download the model file from GCS into a temporary file
    with tempfile.NamedTemporaryFile(suffix=".h5") as temp_model_file:
        blob = bucket.blob(gcs_source_path)
        blob.download_to_filename(temp_model_file.name)

        # Use the downloaded temporary file as the model path
        Model = Prediction(
            model_path=temp_model_file.name, target_size=(224, 224), classes=LABELS
        )
except Exception as e:
    logger.error(f"Error reading from GCS: {e}")
