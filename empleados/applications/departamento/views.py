from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView

from applications import departamento
from .forms import NewDepartamentoForm

from applications.persona.models import Empleado
from .models import Departamento

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        depart = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shor_name']
        )
        depart.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            name = nombre,
            last_name = apellido,
            job='1',
            departamento=depart
        )
        return super(NewDepartamentoView, self).form_valid(form)