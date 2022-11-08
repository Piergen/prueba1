from django.db import models as mod

# Create your models here.

class familiares(mod.Model):
    nombre_completo = mod.CharField(max_length=40)
    edad = mod.IntegerField()
    fecha_nacimiento = mod.DateField()