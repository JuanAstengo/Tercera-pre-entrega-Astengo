"""
URL configuration for gestion_biblioteca project.

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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from biblioteca.views import agregar_usuario, agregar_libro, agregar_prestamo, buscar_libro, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar_usuario/', agregar_usuario, name='agregar_usuario'),
    path('agregar_libro/', agregar_libro, name='agregar_libro'),
    path('agregar_prestamo/', agregar_prestamo, name='agregar_prestamo'),
    path('buscar_libro/', buscar_libro, name='buscar_libro'),
    path('', index, name='index'),  # Asegura que esta ruta apunte a la vista correcta
]
