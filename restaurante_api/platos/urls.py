from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PlatoViewSet

router = DefaultRouter()
router.register(r'', PlatoViewSet)  # Deja la ruta vacía para usar el prefijo 'platos'

urlpatterns = [
    path('', include(router.urls)),  # Usar el router
]
