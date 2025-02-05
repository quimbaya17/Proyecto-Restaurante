# facturacion/models.py
from django.db import models
from pedidos.models import Pedido

class Factura(models.Model):
    FORMA_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    ]
    
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)  # Clave foránea única hacia Pedido
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago = models.CharField(max_length=20, choices=FORMA_PAGO, default='efectivo')
    fecha_factura = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Factura #{self.id} - Pedido #{self.pedido.id} - Monto: {self.monto_total}"
