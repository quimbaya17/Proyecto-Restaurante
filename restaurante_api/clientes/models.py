from django.db import models

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.nombre} - Cédula: {self.cedula}"
