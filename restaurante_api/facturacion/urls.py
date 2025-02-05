from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FacturaViewSet

router = DefaultRouter()
router.register(r'', FacturaViewSet)  # Deja la ruta vacía para usar el prefijo 'facturacion'

urlpatterns = [
    path('', include(router.urls)),  # Usar el router
]
