from django.contrib import admin
from .models import Plato

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_plato', 'precio', 'tipo', 'tamaño')
    search_fields = ('nombre_plato',)
