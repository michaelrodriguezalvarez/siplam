# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mod_control_produccion_indicadores.models import Tecnologia,Emplazamiento,RegistroDiario
# Register your models here.

admin.site.register(Tecnologia)
admin.site.register(Emplazamiento)
admin.site.register(RegistroDiario)
