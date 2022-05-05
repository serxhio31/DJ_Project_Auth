from django.db import models

# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=256)
    details = models.CharField(max_length=500)
    author =models.CharField(max_length=30)

