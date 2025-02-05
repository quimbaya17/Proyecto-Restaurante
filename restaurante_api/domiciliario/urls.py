from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ConductorViewSet

router = DefaultRouter()
router.register(r'', ConductorViewSet)  # Deja la ruta vacía para usar el prefijo 'domiciliarios'

urlpatterns = [
    path('', include(router.urls)),  # Usar el router
]
