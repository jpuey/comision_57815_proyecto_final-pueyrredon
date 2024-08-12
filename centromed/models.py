from django.db import models

# Create your models here.


class Medico(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    matricula = models.IntegerField()
    especialidad= models.CharField (max_length=20)
    email= models.EmailField()

class Paciente (models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    ident= models.IntegerField()
    email= models.EmailField()
    habitacion= models.IntegerField()

class Obrasocial(models.Model):
    nombre= models.CharField (max_length=20)
    plan= models.IntegerField()
    cobertura= models.BooleanField()

class Farmacia (models.Model):
    medicamento= models.CharField(max_length= 20)
    droga= models.CharField (max_length= 20)
    receta= models.BooleanField()

