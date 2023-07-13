from django.db import models

# Create your models here.

class Libros(models.Model):
    nombre=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    codigo= models.CharField(max_length=10)
    estado=models.CharField(max_length=2)
    def __str__(self):
        return self.nombre

   
    