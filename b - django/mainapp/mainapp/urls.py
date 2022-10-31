"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from webapp.views import principal
from gestorapp.views import alumno, editaralumno, agregaralumno, detallealumno, eliminaralumno, maestro,editarmaestro,agregarmaestro, detallemaestro, eliminarmaestro,tutoria,editartutoria, agregartutoria, eliminartutorias, detalletutoria
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',principal, name='index'),
    path('alumno/',alumno,name='alumno'),
    path('alumno/detalle_alumno/<int:id>', detallealumno),
    path('alumno/agregar_alumno', agregaralumno),
    path('alumno/editar_alumno/<int:id>', editaralumno),
    path('alumno/eliminar_alumno/<int:id>',eliminaralumno),
    path('maestro/',maestro,name='maestro'),
    path('maestro/detalle_maestro/<int:id>', detallemaestro),
    path('maestro/agregar_maestro', agregarmaestro),
    path('maestro/editar_maestro/<int:id>', editarmaestro),
    path('maestro/eliminar_maestro/<int:id>',eliminarmaestro),
    path('tutoria/',tutoria,name='tutoria'),
    path('tutoria/detalle_tutoria/<int:id>', detalletutoria),
    path('tutoria/agregar_tutoria', agregartutoria),
    path('tutoria/editar_tutoria/<int:id>', editartutoria),
    path('tutoria/eliminar_tutoria/<int:id>',eliminartutorias)
]
