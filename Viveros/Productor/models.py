from django.db import models

# Create your models here.

class Productor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_documento = models.IntegerField()
    