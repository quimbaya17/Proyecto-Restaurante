
from django.db import models
from clientes.models import Cliente
from domiciliario.models import Conductor
from platos.models import Plato

class Pedido(models.Model):
    ESTADO_PEDIDO = [
        ('preparacion', 'En preparación'),
        ('camino', 'En camino'),
        ('entregado', 'Entregado'),
       
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    fecha_pedido = models.DateField(auto_now_add=True)
    hora_pedido = models.TimeField(auto_now_add=True)
    direccion_entrega = models.CharField(max_length=50)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2)  
    estado_pedido = models.CharField(max_length=20, choices=ESTADO_PEDIDO, default='preparacion')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, null=True, blank=True)  # Clave foránea hacia Conductor

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre}"
    


    # pedidos/models.py (mismo archivo que Pedido)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Clave foránea hacia Pedido
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)  # Clave foránea hacia Plato
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio en pesos colombianos por plato

    def __str__(self):
        return f"{self.cantidad} x {self.plato.nombre_plato} para el pedido #{self.pedido.id}"

