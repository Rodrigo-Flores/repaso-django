from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=100, default='')
    apellido = models.CharField(max_length=200, default='')
    edad = models.IntegerField(default=-1)

    def __str__(self):
        return str(self.nombre)


class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, default='Sin Marca')
    patente = models.CharField(max_length=6, default='Sin Patente')

    def __str__(self):
        return self.patente
