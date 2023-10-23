from django.contrib import admin
from .models import Torneo
# Register your models here.
class TorneoAdmin(admin.ModelAdmin):
    list_display=("nombre","deporte","descripcion","fecha_inicio","fecha_final")
    list_filter=("deporte",)
    search_fields=("fecha_inicio","deporte","nombre")

admin.site.register(Torneo, TorneoAdmin)