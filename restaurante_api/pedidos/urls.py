from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PedidoViewSet

router = DefaultRouter()
router.register(r'', PedidoViewSet)  # Deja la ruta vacía para usar el prefijo 'pedidos'

urlpatterns = [
    path('', include(router.urls)),  # Usar el router
]
