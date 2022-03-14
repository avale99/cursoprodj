from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """ Managers para modelo autor """

    def listar_autores(self):
        return self.all()
    
    def buscar_autor(self, keyword):
        resultado = self.filter(
            nombre__icontains=keyword
        )
        return resultado

    def buscar_autor2(self, keyword):
        resultado = self.filter(
            Q(nombre__icontains=keyword) | Q(apellidos__icontains=keyword)
        )
        return resultado
    
    def buscar_autor3(self, keyword):
        resultado = self.filter(
            nombre__icontains=keyword
        ).exclude(
            Q(edad=35) | Q(edad=43)
        )
        return resultado

    def buscar_autor4(self, keyword):
        resultado = self.filter(
            edad__gt = 40,
            edad__lt = 70
        ).order_by('nombre')
        return resultado