from django import forms
from apps.productos.models import Entradas

class Entradasform(forms.ModelForm):
    class Meta:
        model= Entradas
        
        fields = {
            'fecha',
            'cantidad',
            'valor',
            'productosid',
        }
        
        labels = {
            'fecha': 'ingrese la fecha',
            'cantidad': 'ingrese la de unidades',
            'valor': 'ingrese el valor del producto',
            'productosid': 'Seleccione su producto',
        }
        
        widges = {
            'fecha' : forms.DateInput(attrs={'class': 'form-control'}),
            'cantidad' : forms.IntegerField(),
            'valor' : forms.IntegerField(),
            'ProductoId' : forms.Select(attrs={'class': 'form-control'}),
        }