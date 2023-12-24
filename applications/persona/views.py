from django.shortcuts import render
from django.views.generic import (
    ListView
)

# modelos
from .models import Empleado

# listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    model = Empleado
    template_name = "persona/list_all.html"
    context_object_name = 'lista_all_empleados'

# listar todos los empleados de la empresa que pertenecen a un area

class ListByAreaEmpleado(ListView):
    template_name = "persona/list_by_area.html"
    queryset = Empleado.objects.filter(
        departamento__shor_name='Otro'
    )
    context_object_name = 'lista_by_area'

# listar empleados por trabajo
# listar empleados por palabra clave
# listar habilidades de un  empleado