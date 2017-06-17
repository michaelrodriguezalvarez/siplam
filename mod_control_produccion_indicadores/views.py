# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from mod_control_produccion_indicadores.models import RegistroDiario,Emplazamiento

def index(request):
    return render(request,'index.html')

def consumo_especifico_combustible(request):
    registro = RegistroDiario.objects.filter(emplazamiento=Emplazamiento.objects.filter(nombre='Guacara').first().pk,fecha='2017-06-17').first()
    return render(request,'consumos/consumo_especifico_combustible.html',{'registro':registro})