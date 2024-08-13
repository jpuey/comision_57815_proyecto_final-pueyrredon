from django.urls import path
from centromed.views import *

urlpatterns = [
    path("", inicio, name="index"),
    path("medicos", medicos, name= "medicos"),
    path("pacientes", pacientes, name= "pacientes"),
    path("osociales", osociales, name= "osociales"),
    path("farmacias", farmacias, name= "farmacias"),
    path("about", abouts, name= "about"),
    
]


formularios =[
    path("form-medico", medicoFormulario, name="form-medico"),
    path("form-paciente", pacienteFormulario, name="form-paciente"),
    path("form-farmacia", farmaciaFormulario, name="form-farmacia"),



]

urlpatterns += formularios