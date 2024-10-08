from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from users.forms import *
from users.models import Avatar


# Create your views here.

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "centromed/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"centromed/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})

@login_required
def editar_perfil (request):
    usuario = request.user

    if request.method == "POST":
        mi_formulario= UserEditForm(request.POST, request.FILES, instance=usuario)
        if mi_formulario.is_valid():
            if mi_formulario.cleaned_data.get('imagen'):
                if Avatar.objects.filter(user=usuario).exists():
                    usuario.avatar.imagen =  mi_formulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    image= Avatar(user=usuario, imagen=mi_formulario.cleaned_data.get('imagen'))
                    image.save()


            mi_formulario.save()
            return render(request, "centromed/index.html")
    else:
        mi_formulario = UserEditForm(instance=usuario)
    
    return render (request, "users/editar_perfil.html", {"form":mi_formulario})

class CambiarConstrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name= 'users/editar_pass.html'
    success_url= reverse_lazy("EditarPerfil")

