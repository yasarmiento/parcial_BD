from django.db import models

# Create your models here.

class Productos (models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre

class Entradas (models.Model):
    fecha = models.DateField()
    cantidad = models.CharField(max_length=30)
    valor = models.IntegerField()
    productosid = models.ForeignKey(Productos, on_delete=models.CASCADE)
    