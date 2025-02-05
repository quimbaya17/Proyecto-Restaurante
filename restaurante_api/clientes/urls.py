from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClienteViewSet

router = DefaultRouter()
router.register(r'', ClienteViewSet)  # Deja la ruta vacía para usar el prefijo 'clientes'

urlpatterns = [
    path('', include(router.urls)),  # Usar el router
]
