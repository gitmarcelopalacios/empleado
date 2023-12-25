from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(),name='listar_todo_empleado'),
    path('lista-by-area/<shorname>/', views.ListByAreaEmpleado.as_view(),name='lista_by_area'),
    path('buscar-empleado/', views.ListEmpleadoByKword.as_view(),name='lista_by_area'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)