from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Materia {self.id}: {self.nombre}'

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    noExterior = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Calle {self.calle}, noExterior {self.noExterior}, colonia {self.colonia}'

class Alumno(models.Model):
    nombre= models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
    materia = models.ForeignKey(Materia,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Alumno {self.id}: {self.nombre}, domicilio {self.domicilio}, materia {self.materia}'

class Maestro(models.Model):
    nombre= models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
    materia = models.ForeignKey(Materia,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Maestro {self.id} {self.nombre}, materia {self.materia}'

class Tutorias (models.Model):
    maestro = models.ForeignKey(Maestro,on_delete=models.SET_NULL,null=True)
    alumno = models.ForeignKey(Alumno,on_delete=models.SET_NULL,null=True)
    observaciones = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Tutorias: maestro: {self.maestro}, alumno:{self.alumno}, observaciones: {self.observaciones}'