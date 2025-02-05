from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes.views import ClienteViewSet
from platos.views import PlatoViewSet
from pedidos.views import PedidoViewSet
from domiciliario.views import ConductorViewSet
from facturacion.views import FacturaViewSet

# Definir el router de DRF
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'platos', PlatoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'domiciliarios', ConductorViewSet)
router.register(r'facturacion', FacturaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Incluir todas las rutas del router
]
