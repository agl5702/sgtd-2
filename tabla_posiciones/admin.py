from django.contrib import admin
from tabla_posiciones.models import TablaPosiciones
# Register your models here.
    
class TPosicionesAdmin(admin.ModelAdmin):
    list_display = ('puntos', 'victorias', 'derrotas','goles_a_favor', 'goles_en_contra')


admin.site.register(TablaPosiciones,TPosicionesAdmin)
