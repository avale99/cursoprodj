from django.db import models
from applications.autor.models import Autor
from .managers import LibrosManager, CategoriaManager

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=50, blank=True,
        null=True)

    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) +" - " + self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name='categoria_libro'
    )

    autores = models.ManyToManyField(Autor)

    titulo = models.CharField('Titulo', max_length=50)
    fecha = models.DateField('Fecha Lanzamiento')
    portada = models.ImageField(upload_to='portada', blank=True, null=True)
    visitas = models.PositiveIntegerField('Visitas')

    objects = LibrosManager()

    def __str__(self):
        return str(self.id) + " - " + self.titulo

