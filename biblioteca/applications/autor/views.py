from django.shortcuts import render
from django.views.generic import ListView
from .models import Autor

# Create your views here.
class ListAutoresListView(ListView):
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("keyword", '')
        return Autor.objects.buscar_autor4(palabra_clave)
    


