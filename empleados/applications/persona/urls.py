from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name="inicio"),
    path('lista-empleados/', views.ListAllEmpleados.as_view(), name="empleados_all"),
    path('lista-empleados-area/<shorname>/', views.ListByAreaEmpleados.as_view(), name="empleados_area"),
    path('lista-empleados-admin', views.ListEmpleadosAdmin.as_view(), name="empleados_admin"),
    path('buscar-empleado/', views.ListEmpleadosByKWord.as_view()),
    path('lista-habilidades/', views.ListHabilidadesEmpleados.as_view()),
    #CRUD
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name="empleado_detail"),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name="crear_empleado"),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar'),
    path('delete/<pk>/', views.EmpleadoDeleteView.as_view(), name='delete'),
]