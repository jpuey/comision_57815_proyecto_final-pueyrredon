from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse ("Este es el Inicio")

def medicos(request):
    return HttpResponse ("Esta es la vista de los medicos")

def pacientes (request):
    return HttpResponse ("Esta es la vista de los pacientes")

def osociales (request):
    return HttpResponse ("Esta es la vista de las Obras Sociales")

def farmacias (request):
    return HttpResponse ("Esta es la vista de la Farmacia")

