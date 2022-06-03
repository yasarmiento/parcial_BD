
from django.shortcuts import render, redirect
from apps.productos.formentradas import Entradasform
from apps.productos.models import Entradas

# Create your views here.

def inicio(request):    
    entradas = Entradas.objects.all().order_by('id')
    return render(request,'paginas/entradas.html', {'entradas': entradas})

def create(request):
    if request.method == 'POST':
        form = Entradasform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = Entradasform()
        return render(request,'paginas/entradasform.html', {'form': form})