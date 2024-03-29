
from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# llamo todos los modelo que usare en las vistas
from .models import Empleado
# llamo los forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    template_name="inicio.html"

# listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    #model = Empleado
    template_name = "persona/list_all.html"
    paginate_by=4
    ordering='first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
            )
        return lista 


# administrar crud

class ListEmpleadosAdmin(ListView):
    #model = Empleado
    template_name = "persona/lista_empleados.html"
    paginate_by=6
    ordering='first_name'
    context_object_name = 'empleados'
    model = Empleado


# listar todos los empleados de la empresa que pertenecen a un area

class ListByAreaEmpleado(ListView):
    template_name = "persona/list_by_area.html"
    context_object_name='empleados'

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
        # desde get formulario
        palabra_clave=self.request.GET.get("kword", '')
        lista=Empleado.objects.filter(
             first_name=palabra_clave
        )
        return lista

# listar habilidades de un  empleado

class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name='habilidades'
    def get_queryset(self):
        # selecciono el registro numero 2 de empleado desde tabla
        empleado=Empleado.objects.get(id=2)
        return empleado.habilidades.all()
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    def get_context_data(self, **kwargs):
        context=super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url=reverse_lazy('persona_app:empleados_admin')
    #success_url=reverse_lazy('persona_app:correcto')

    def form_valid(self, form):

        # logica de validacion
        empleado=form.save(commit=False)

        empleado.full_name=empleado.first_name+' '+empleado.last_name

        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    
    model = Empleado
    
    template_name ="persona/update.html"
    
    fields=['first_name','last_name','job','departamento','habilidades']
    
    success_url=reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):

        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    
    model = Empleado
    
    template_name ="persona/delete.html"
    
    success_url=reverse_lazy('persona_app:empleados_admin')

 