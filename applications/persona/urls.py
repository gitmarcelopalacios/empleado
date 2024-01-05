from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'lista-by-area/<shorname>/', 
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'
    ),
    path(
        'buscar-empleado/', 
        views.ListEmpleadoByKword.as_view(),
        name='lista_by_area'
    ),
    path(
        'lista-habilidades-empleado/', 
        views.ListHabilidadesEmpleado.as_view(),
        name='lista_habilidades_empleado'
    ),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='add_empleado'
    ),
    path(
        'success/', 
        views.SuccessView.as_view(),
        name='correcto',
    ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado',
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado',
    ),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)