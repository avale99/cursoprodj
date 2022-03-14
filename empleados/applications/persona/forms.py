from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = (
            'name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
            'image'
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
