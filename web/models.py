from django.db import models

# Create your models here.
class Data(models.Model):
    value = models.CharField(max_length=100)