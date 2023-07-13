from django import forms
from LibrosApp .models import Libros

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['codigo', 'nombre', 'precio', 'estado', 'descripcion']
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'codigo': 'Codigo',
            'descripcion': 'Descripcion',  # Agrega una coma al final de esta línea
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
