from django.urls import path
from centromed.views import *

urlpatterns = [
    path("", inicio, name="index"),
    path("medicos", medicos, name= "medicos"),
    path("pacientes", pacientes, name= "pacientes"),
    path("osociales", osociales, name= "osociales"),
    path("farmacias", farmacias, name= "farmacias"),
    path("about", abouts, name= "about")
]
