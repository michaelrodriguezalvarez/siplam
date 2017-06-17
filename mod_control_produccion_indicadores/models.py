# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Comienzo Nomencladores

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Emplazamiento(models.Model):
    nombre = models.CharField(max_length=250)
    tecnologia = models.ForeignKey('Tecnologia', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#Fin Nomencladores

class RegistroDiario(models.Model):
    emplazamiento = models.ForeignKey('Emplazamiento',models.CASCADE)
    consumo_combustible = models.DecimalField(max_digits=6,decimal_places=0)
    energia_generada = models.DecimalField(max_digits=6,decimal_places=0)
    consumo_aceite_motor = models.DecimalField(max_digits=6,decimal_places=0)
    consumo_agua = models.DecimalField(max_digits=6,decimal_places=0)
    fecha = models.DateField()

    def __str__(self):
        return str(self.emplazamiento) +' '+ str(self.fecha)