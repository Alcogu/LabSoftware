from django import forms
from Vivero.models import Vivero
from colorfield.widgets import ColorWidget 

class FormularioVivero(forms.ModelForm):
    
    #Se crea la clase para invocar el modelo 
    class Meta:
        model = Vivero 
        #fields = '__all__'

    #Se crear tuplas para guardar la información o los campos del modelo
        fields =[
            'id',
            'codigo',
            'nombre',
            'id_productor',
            'id_departamento',
        ]
    #Se definen las etiquetas y escribimos un diccionario

        labels = {
            'id': 'ID',
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'id_productor': 'ID productor',
            'id_departamento': 'ID departamento',
        }

        widgets = {
            'id': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder':'Ingrese el id del vivero',
                    'autofocus': 'autofocus'}),

            'codigo': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese el codigo del vivero', 
                'autofocus': 'autofocus'}),

            'nombre': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese el nombre del vivero', 
                'autofocus': 'autofocus'}),

            'id_productor': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese el ID del productor', 
                'autofocus': 'autofocus'}),

            'id_departamento': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese el ID del departamento', 
                'autofocus': 'autofocus'}),
        }