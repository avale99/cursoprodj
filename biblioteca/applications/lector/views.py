from django.shortcuts import render
from django.views.generic import ListView
from .models import Lector

# Create your views here.
class ListLectoresListView(ListView):
    context_object_name = 'lista_lectores'
    template_name = 'lector/listar.html'

    def get_queryset(self):
        return Lector.objects.listar_lectores()
    