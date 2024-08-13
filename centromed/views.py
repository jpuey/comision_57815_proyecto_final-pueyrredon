from django.shortcuts import render
from django.http import HttpResponse
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