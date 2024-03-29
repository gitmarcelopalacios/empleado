"""
URL configuration for empleado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view(), name='home'),
    path('lista/', views.PruebaListView.as_view(), name='lista'),
    path('lista-prueba/', views.ModeloPruebaListView.as_view(), name='lista_prueba'),
    path(
        'add/', 
        views.PruebaCreateView.as_view(), 
        name='prueba_add'
        ),
    path(
        'resume-foundation/', 
        views.ResumeFoundationView.as_view(), 
        name='resume_foundation'
        ),
    path(
        'home1/', 
        views.HomeTemplate1View.as_view(), 
        name='home1'
        ),
    
    path(
        'home2/', 
        views.HomeTemplate2View.as_view(), 
        name='home2'
        ),
    
    path(
        'home3/', 
        views.HomeTemplate3View.as_view(), 
        name='home3'
        ),
    
]
