from django import forms
from Productor.models import Productor

class FormularioProductor(forms.Form):
    
    #Se cre la clase para invocar el modelo 
    class Meta:
        model = Productor 

    #Se crear tuplas para guardar la información o los campos del modelo
        fields =[
            'numero_documento',
            'nombre',
            'apellido',
            'direccion',
            'email',
            'telefono',
        ]
    #Se definen las etiquetas y escribimos un diccionario

        labels = [
            'numero_documento': 'N° Docuemtno',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'direccion': 'Direccion',
            'email': 'Email',
            'telefono': 'Telefono',
        ]

        widgets = [
            'numero_documento': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
        ]

    
    
    
    '''numero_documento = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=60)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=10)'''

    