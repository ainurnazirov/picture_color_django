from django.db import models

# Create your models here.
class Image(models.Model):
    color = models.CharField(max_length=7)
    image = models.ImageField()