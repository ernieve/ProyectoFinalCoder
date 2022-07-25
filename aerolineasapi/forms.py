from dataclasses import fields
from django import forms
from django.core import validators
from django.contrib.auth.forms import * 
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nombre usuario",validators=[
            validators.MinLengthValidator(2,'Usuario muy corto'),
            validators.RegexValidator('^[A-Za-z0-9Ññ]*$','Por favor ingresa solo letras o numeros'),
            ])
    first_name = forms.CharField(label="Nombre",validators=[
            validators.MinLengthValidator(2,'El nombre es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9Ññ]*$','Por favor ingresa solo letras o numeros'),
            ])
    last_name = forms.CharField(label="Apellido",validators=[
            validators.MinLengthValidator(2,'El es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9Ññ]*$','Por favor ingresa solo letras o numeros'),
            ])
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ChangeForm(UserChangeForm):
    first_name = forms.CharField(label="Nombre",validators=[
            validators.MinLengthValidator(2,'El nombre es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9Ññ]*$','Por favor ingresa solo letras o numeros'),
            ])
    last_name = forms.CharField(label="Apellido",validators=[
            validators.MinLengthValidator(2,'El es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9Ññ]*$','Por favor ingresa solo letras o numeros'),
            ])
    class Meta():
        model = User
        fields = ('email','first_name','last_name',)

class ShowForm(forms.Form):
    first_name = forms.CharField(label="Nombre",disabled=True)
    last_name = forms.CharField(label="Apellido",disabled=True)
    email = forms.CharField(label="Email",disabled=True)
    #is_staff = forms.CharField(label="Staff",disabled=True)
    class Meta():
        model = User
        fields = ('email','first_name','last_name',)#'is_staff',)    

class FormArticulo(forms.Form):
    corta_desc = forms.CharField(max_length=50,label="descripcion",)
    content = forms.CharField(widget=forms.Textarea,label="Contenido") 

#Formulario avion
class NuevoAvion(forms.Form):
    modelo = forms.CharField(max_length=30,label="Nombre de avion")
    modelo.widget.attrs.update({'placeholder':'Nombre modelo'})
    fabricante = forms.CharField(
        label='Fabricante'
        ,max_length=110
    )
    fabricante.widget.attrs.update({'placeholder':'Nombre fabricante'})
    anio = forms.IntegerField(min_value=0, label="Año")
    anio.widget.attrs.update({'placeholder':'Año'})
    #Para el menu de seleccion que sera de dos opciones nada mas
    opciones =[(1,'Si'),(0,'No')]
    #Este metodo me permite mostrar un campo select
    estado = forms.TypedChoiceField(label='¿Activo?',choices = opciones)

class ShowForms(forms.Form):
    # id = forms.CharField(label="id",disabled=True)
    modelo = forms.CharField(label="Modelo",disabled=True)
    fabricante = forms.CharField(label="fabricante",disabled=True)
    anio = forms.CharField(label="anio",disabled=True)
    estado = forms.TypedChoiceField(label="¿Activo?",disabled=True)
    class Meta():
        model = User
        fields = ('modelo','fabricante','anio','estado')
