from django.db import models
from partidos_horarios.models import Partido
# Create your models here.
class TablaPosiciones(models.Model):
    puntos= models.IntegerField(default=0)
    victorias=models.IntegerField(default=0)
    derrotas=models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)


class Tabla_Partidos(models.Model):
    tablas_partidos= models.ManyToManyField(TablaPosiciones)
    partido= models.ManyToManyField(Partido)


