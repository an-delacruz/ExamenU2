from django.contrib import admin
from gestorapp.models import Materia, Domicilio, Alumno, Maestro, Tutorias
# Register your models here.

admin.site.register(Materia) #subentidad
admin.site.register(Domicilio) #subtenidad
admin.site.register(Alumno) #entidad
admin.site.register(Maestro) #entidad
admin.site.register(Tutorias) #entidad
