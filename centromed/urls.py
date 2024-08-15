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
    path("form-osociales", obrasocialFormulario, name="form-osociales"),
    path("busqueda-especialidad",busquedaEspecialidad, name="busqueda-especialidad"),

    path("medico_lista", MedicoListView.as_view(), name= "medico_lista"),
    path("medico_crear", MedicoCreateView.as_view(), name= "medico_crear"),

    path("paciente_lista", PacienteListView.as_view(), name= "paciente_lista"),
    path("paciente_crear", PacienteCreateView.as_view(), name= "paciente_crear"),

    path("osociales_lista", ObrasocialListView.as_view(), name= "osociales_lista"),
    path("osociales_crear", ObrasocialCreateView.as_view(), name= "osociales_crear"),

    path("farmacia_lista", FarmaciaListView.as_view(), name= "farmacia_lista"),
    path("farmacia_crear", FarmaciaCreateView.as_view(), name= "farmacia_crear"),



]




urlpatterns += formularios