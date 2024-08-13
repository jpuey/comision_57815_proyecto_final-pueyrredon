from django.db import models

# Create your models here.


class Medico(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    matricula = models.IntegerField()
    especialidad= models.CharField (max_length=20)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre del Profesional: {self.nombre} - Matricula: {self.matricula}"

class Paciente (models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    ident= models.IntegerField()
    email= models.EmailField()
    habitacion= models.IntegerField()

    def __str__(self):
        return f"Nombre del Paciente: {self.nombre} - Identificacion del Paciente: {self.ident}"

class Obrasocial(models.Model):
    nombre= models.CharField (max_length=20)
    plan= models.IntegerField()
    cobertura= models.BooleanField()

    def __str__(self):
        return f"Nombre de la Obra Social: {self.nombre} - Cobertura de la Obra Social: {self.cobertura}"

class Farmacia (models.Model):
    medicamento= models.CharField(max_length= 20)
    droga= models.CharField (max_length= 20)
    receta= models.BooleanField()

    def __str__(self):
        return f"Nombre del Medicamento: {self.medicamento} - Droga: {self.droga}"

