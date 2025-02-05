from django.db import models

class Plato(models.Model):
    # Categorías de platos
    TIPO_ARROZ = 'arroz'
    TIPO_COMBO = 'combo'
    
    TIPO_OPCIONES = [
        (TIPO_ARROZ, 'Arroz'),
        (TIPO_COMBO, 'Combo'),
    ]

    # Opciones de tamaño o combos
    TAMANO_PERSONAL = 'personal'
    TAMANO_DOS_PERSONAS = 'dos_personas'
    TAMANO_CUATRO_PERSONAS = 'cuatro_personas'
    TAMANO_SEIS_PERSONAS = 'seis_personas'
    COMBO_FAMILIAR = 'combo_familiar'
    COMBO_PERSONAL = 'combo_personal'
    
    TAMANO_OPCIONES = [
        (TAMANO_PERSONAL, 'Personal (400g)'),
        (TAMANO_DOS_PERSONAS, 'Para dos personas (700g)'),
        (TAMANO_CUATRO_PERSONAS, 'Para cuatro personas (1500g)'),
        (TAMANO_SEIS_PERSONAS, 'Para seis personas (2500g)'),
        (COMBO_FAMILIAR, 'Combo familiar + gaseosa 1.5L'),
        (COMBO_PERSONAL, 'Combo personal + gaseosa + consomé'),
    ]

    # Campos del modelo
    nombre_plato = models.CharField(max_length=80)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio en pesos colombianos
    tipo = models.CharField(max_length=10, choices=TIPO_OPCIONES)
    tamaño = models.CharField(max_length=20, choices=TAMANO_OPCIONES)

    def __str__(self):
        return f"{self.nombre_plato} ({self.get_tamaño_display()})"
