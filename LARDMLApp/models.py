from django.db import models

# Create your models here.
class PredictionResult(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    prediction = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name