from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate



from centromed.forms import *
from centromed.models import *

# Create your views here.

def inicio(request):
    return render(request,"centromed/index.html" )

def medicos(request):
    return render (request, "centromed/medicos.html")

def pacientes (request):
    return render(request, "centromed/pacientes.html")

def osociales (request):
    return render (request, "centromed/osociales.html")

def farmacias (request):
    return render (request, "centromed/farmacias.html")

def abouts (request):
    return render (request, "centromed/about.html")


def medicoFormulario(request):

    if request.method == "POST":

            miFormulario = MedicoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                medico = Medico(nombre=informacion["nombre"], apellido =informacion["apellido"], matricula=informacion["matricula"], especialidad=informacion["especialidad"], email=informacion["email"] )
                medico.save()
                return render(request, "centromed/medicos.html")
    else:
            miFormulario = MedicoFormulario()

    return render(request, "centromed/form-medico.html", {"miFormulario": miFormulario})

def pacienteFormulario(request):

    if request.method == "POST":

            miFormulario = PacienteFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                paciente = Paciente(nombre=informacion["nombre"], apellido =informacion["apellido"], ident=informacion["ident"], habitacion=informacion["habitacion"], email=informacion["email"] )
                paciente.save()
                return render(request, "centromed/pacientes.html")
    else:
            miFormulario = PacienteFormulario()

    return render(request, "centromed/form-paciente.html", {"miFormulario": miFormulario})


def farmaciaFormulario(request):

    if request.method == "POST":

            miFormulario = FarmaciaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                farmacia = Farmacia(medicamento=informacion["medicamento"], droga =informacion["droga"], receta=informacion["receta"])
                farmacia.save()
                return render(request, "centromed/farmacias.html")
    else:
            miFormulario = FarmaciaFormulario()

    return render(request, "centromed/form-farmacia.html", {"miFormulario": miFormulario})


def obrasocialFormulario(request):

    if request.method == "POST":

            miFormulario = ObrasocialFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                osocial= Obrasocial(nombre=informacion["nombre"], plan=informacion["plan"], cobertura=informacion["cobertura"])
                osocial.save()
                return render(request, "centromed/osociales.html")
    else:
            miFormulario = ObrasocialFormulario()

    return render(request, "centromed/form-osociales.html", {"miFormulario": miFormulario})



def busquedaEspecialidad(request):
    if request.method == "POST":
        mi_formulario = BuscaMedicoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            
            medicos = Medico.objects.filter(especialidad__icontains=informacion["especialidad"])

            return render(request, "centromed/mostrar-especialidad.html", {"medicos": medicos})
    else:
        mi_formulario = BuscaMedicoForm()

    return render(request, "centromed/busqueda-especialidad.html", {"mi_formulario": mi_formulario})


#Medicos

class MedicoListView(ListView):
    model = Medico
    context_object_name = "medicos"
    template_name = "centromed/medico_lista.html"


class MedicoCreateView(CreateView):
    model= Medico
    template_name= "centromed/medico_crear.html"
    success_url= reverse_lazy("medico_lista")
    fields= ["nombre","apellido","especialidad", "matricula", "email"]

class MedicoUpdateView(UpdateView):
    model= Medico
    template_name= "centromed/medico_update.html"
    success_url= reverse_lazy("medico_lista")
    fields= ["nombre","apellido","especialidad", "matricula", "email"]

class MedicoDeleteView(DeleteView):
    model= Medico
    template_name= "centromed/medico_delete.html"
    success_url= reverse_lazy("medico_lista")

class MedicoDetailView(DetailView):
    model= Medico
    template_name= "centromed/medico_detail.html"


        
#Pacientes

class PacienteListView(ListView):
    model= Paciente
    context_object_name = "pacientes"
    template_name = "centromed/paciente_lista.html"


class PacienteCreateView(CreateView):
    model= Paciente
    template_name= "centromed/paciente_crear.html"
    success_url= reverse_lazy("paciente_lista")
    fields= ["nombre","apellido","ident", "habitacion", "email"]

class PacienteUpdateView(UpdateView):
    model= Paciente
    template_name= "centromed/paciente_update.html"
    success_url= reverse_lazy("paciente_lista")
    fields= ["nombre","apellido","ident", "habitacion", "email"]

class PacienteDeleteView(DeleteView):
    model= Paciente
    template_name= "centromed/paciente_delete.html"
    success_url= reverse_lazy("paciente_lista")

class PacienteDetailView(DetailView):
    model= Paciente
    template_name= "centromed/paciente_detail.html"

#Obras Sociales

class ObrasocialListView(ListView):
    model= Obrasocial
    context_object_name = "obras_sociales"
    template_name = "centromed/osociales_lista.html"


class ObrasocialCreateView(CreateView):
    model= Obrasocial
    template_name= "centromed/osociales_crear.html"
    success_url= reverse_lazy("osociales_lista")
    fields= ["nombre","plan","cobertura"]

class ObrasocialUpdateView(UpdateView):
    model= Obrasocial
    template_name= "centromed/osociales_update.html"
    success_url= reverse_lazy("osociales_lista")
    fields= ["nombre","plan","cobertura"]

class ObrasocialDeleteView(DeleteView):
    model= Obrasocial
    template_name= "centromed/osociales_delete.html"
    success_url= reverse_lazy("osociales_lista")

class ObrasocialDetailView(DetailView):
    model= Obrasocial
    template_name= "centromed/osociales_detail.html"
    

#Farmacia

class FarmaciaListView(ListView):
    model= Farmacia
    context_object_name = "farmacias"
    template_name = "centromed/farmacia_lista.html"


class FarmaciaCreateView(CreateView):
    model= Farmacia
    template_name= "centromed/farmacia_crear.html"
    success_url= reverse_lazy("farmacia_lista")
    fields= ["medicamento","droga","receta"]

class FarmaciaUpdateView(UpdateView):
    model= Farmacia
    template_name= "centromed/farmacia_update.html"
    success_url= reverse_lazy("farmacia_lista")
    fields= ["medicamento","droga","receta"]

class FarmaciaDeleteView(DeleteView):
    model= Farmacia
    template_name= "centromed/farmacia_delete.html"
    success_url= reverse_lazy("farmacia_lista")

class FarmaciaDetailView(DetailView):
    model= Farmacia
    template_name= "centromed/farmacia_detail.html"
