from django.db import models
from Productor.models import Productor

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'departamento'
        verbose_name_plural = 'departamentos'


class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'


class Vivero(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'vivero'
        verbose_name_plural = 'viveros'


