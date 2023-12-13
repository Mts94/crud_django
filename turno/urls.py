"""
URL configuration for turno project.

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
from appturnos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('login/', views.inicio_sesion,name= 'login'),
    path('reserva/', views.reserva ,name= 'reserva'),
    path('eventos_realizados/', views.eventos_completados ,name= 'completados'),
    path('crear/reserva/', views.crear_res,name= 'crear'),
    path('reserva/<int:res_id>/', views.eventos_detalles, name='detalles'),
    path('reserva/<int:res_id>/realizado', views.evento_realizado, name='realizado'),
    path('reserva/<int:res_id>/borrar/', views.eliminar, name='borrar'),
    path('logout/', views.cerrar_sesion ,name= 'logout'),
    path('registro/',views.registro, name= 'registro'),
    
]
   
