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
    context_object_name='lista'

    def get_queryset(self):
        area=self.kwargs['shorname']
        lista=Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista

# listar empleados por palabra clave

class ListEmpleadoByKword(ListView):
    template_name = "persona/by_kword.html"
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword", '')
        lista=Empleado.objects.filter(
             first_name=palabra_clave
        )
        return lista




# listar habilidades de un  empleado
# listar empleados por trabajo