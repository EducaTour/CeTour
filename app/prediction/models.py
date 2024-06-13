from django.db import models

class Prediction(models.Model):
    result = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.URLField()
    createdAt = models.DateTimeField(auto_now_add=True)
