from django.contrib import admin

from .models import *

# Register your models here.

class MedicoAdmin(admin.ModelAdmin):
    list_display = ("nombre")
    list_per_page = 10

class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombre")
    list_per_page = 10

class ObrasocialAdmin(admin.ModelAdmin):
    list_display = ("nombre")
    list_per_page = 10

class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ("medicamento")
    list_per_page = 10        

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Farmacia)
admin.site.register(Obrasocial)
