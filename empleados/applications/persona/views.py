from dataclasses import fields
from gc import get_objects
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
#models
from .models import Empleado
#forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ Carga la pagina de inicio """
    template_name = 'inicio.html'
    

#Listar todos los Empleados
#paginate_by es usado para la carga pesada en las bases de datos /?page=X
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    #model = Empleado
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            name__icontains = palabra_clave
        )
        return lista

#Listar todos los Empleados de un Departamento
class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista

#Listar Empleados por Palabra Clave
class ListEmpleadosByKWord(ListView):
    template_name = 'persona/list_by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            name=palabra_clave
        )
        return lista

#Listar Habilidades de Empleado
class ListHabilidadesEmpleados(ListView):
    template_name = 'persona/list_habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()
    
#
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"

#CREATE
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_all')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

#UPDATE
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #request.POST['name']
        return super().post(request, *args, **kwargs)

#DELETE
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 4
    model = Empleado
    context_object_name='empleados'

    