from re import search
from unicodedata import name
from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'last_name',
        'full_name',
        'departamento',
        'job',
    )

    def full_name(self, obj):
        return obj.name + ' ' + obj.last_name

    #
    search_fields = ('name',)
    list_filter = ('job', 'habilidades', 'departamento',)
    #
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)