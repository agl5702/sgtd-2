from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Torneo(models.Model):
    
    usuario= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    nombre= models.CharField(max_length=40)
    deporte= models.CharField(max_length=30)
    descripcion= models.TextField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    def __str__(self):
        return self.nombre
