"""
URL configuration for SaludVida project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import CentroMedico.views as cen


urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('', cen.index, name='home'),
    
    #Especialidades
    path('listar_especialidades/', cen.ListarEspecialidades.as_view(), name='listar_especialidades'),
    path('crear_especialidad/', cen.CrearEspecialidades.as_view(), name='crear_especialidad'),
    path('eliminar_especialidad/<int:pk>', cen.EliminarEspecialidades.as_view(), name='eliminar_especialidad'),
    path('actualizar_especialidad/<int:pk>', cen.ActualizarEspecialidades.as_view(), name='actualizar_especialidad'),

    #Médicos
    path('listar_medicos/', cen.ListarMedicos.as_view(), name='listar_medicos'),
    path('crear_medico/',cen.CrearMedicos.as_view(), name='crear_medico' ),
    path('eliminar_medico/<int:pk>', cen.EliminarMedicos.as_view(), name='eliminar_medico'),
    path('actualizar_medico/<int:pk>', cen.ActualizarMedicos.as_view(), name='actualizar_medico'),
]
