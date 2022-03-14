from django.db import models
from django.db.models import Q

class LectorManager(models.Manager):
    """ Managers para modelo lector """

    def listar_lectores(self):
        return self.all()