import os
import uuid

from django.db import models


def get_file_path(filename):
    ext = filename.split(".")[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("photos/", new_filename)


class Prediction(models.Model):
    result = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to=get_file_path)
    createdAt = models.DateTimeField(auto_now_add=True)
