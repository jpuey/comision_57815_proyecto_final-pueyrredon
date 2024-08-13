from django import forms

class MedicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    matricula = forms.IntegerField()
    especialidad= forms.CharField(max_length=30)
    email= forms.EmailField()


class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    ident= forms.IntegerField()
    email= forms.EmailField()
    habitacion = forms.IntegerField()


class ObrasocialFormulario(forms.Form):
    nombre= forms.CharField (max_length=20)
    plan= forms.IntegerField()
    cobertura= forms.BooleanField(required=False)


class FarmaciaFormulario (forms.Form):
    medicamento= forms.CharField(max_length= 20)
    droga= forms.CharField (max_length= 20)
    receta= forms.BooleanField(required=False)
