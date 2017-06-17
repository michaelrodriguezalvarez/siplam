from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^consumo_especifico_combustible/', views.consumo_especifico_combustible,name='consumo_especifico_combustible'),
]
