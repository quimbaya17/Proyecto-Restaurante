
from django.db import models

class Conductor(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10, unique=True)  # Cédula única
    telefono = models.CharField(max_length=10)
    vehiculo = models.CharField(max_length=10)
    placa = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} - {self.vehiculo} ({self.placa})"
