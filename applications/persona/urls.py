from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="persona_app"

urlpatterns = [
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='listar_todo_empleado'
    ),
    path(
        'lista-by-area/<shorname>/', 
        views.ListByAreaEmpleado.as_view(),
        name='lista_by_area'
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
        name='empleado_detail_view'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='add_empleado'
    ),
    path(
        'success/', 
        views.SuccessView.as_view(),
        name='success',
    ),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)