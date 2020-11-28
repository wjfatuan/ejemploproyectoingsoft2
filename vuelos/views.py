from os import name
from django.shortcuts import render
from django.http import HttpResponse

from .models import Ciudad, Aeropuerto

# Create your views here.
def index(request):
    ciudades = Ciudad.objects.filter(codigo__gte=50)
    datos = {
        'lista_ciudades': ciudades,
    }
    return HttpResponse(render(request, 'ciudades.html', datos))

def aeropuertos(request):
    aeropuertos = Aeropuerto.objects.filter(ciudad__codigo__exact=request.GET.get("ciudad"))
    datos = {
        'lista_ciudades': aeropuertos,
    }
    return HttpResponse(len(aeropuertos))