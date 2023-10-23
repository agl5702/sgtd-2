from django.contrib import admin
from equipo_jugador.models import Equipo, Jugador,Equipo_torneo

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display=('nombre','logo','detalles')
    search_fields=('nombre',)
class JugadorAdmin(admin.ModelAdmin):
    list_display=('nombre','id_jugador','jugador_equipo','numero_ficha')
    search_fields = ('nombre','id_jugador','numero_ficha','jugador_equipo',)


class Equipo_torneoAdmin(admin.ModelAdmin):
    list_display=('equipo','torneo')


admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Jugador,JugadorAdmin)
admin.site.register(Equipo_torneo,Equipo_torneoAdmin)