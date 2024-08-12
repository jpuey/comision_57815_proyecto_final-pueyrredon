from django.urls import path
from centromed.views import *

urlpatterns = [
    path("", inicio, name="index"),
    path("medicos", medicos, name= "medicos"),
    path("pacientes", pacientes, name= "pacientes"),
    path("osociales", osociales, name= "habitaciones"),
    path("farmacias", farmacias, name= "medicamentos"),
]
