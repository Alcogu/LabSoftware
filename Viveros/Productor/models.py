from django.db import models

# Create your models here.

class Productor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
<<<<<<< HEAD
    numero_documento = models.IntegerField()
=======
    numero_documento = models.IntegerField()
    
>>>>>>> dimas