from django.db import models
from applications.libro.models import Libro
from .managers import LectorManager
# Create your models here.

class Lector(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50)
    edad = models.PositiveIntegerField('Edad', default=0)

    objects = LectorManager()

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField('Fecha Prestamo')
    fecha_devolucion = models.DateField('Fecha Devolucion', blank=True, null=True)
    devuelto = models.BooleanField()

    def __str__(self):
        return self.libro.titulo
    
    