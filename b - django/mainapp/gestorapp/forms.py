from tkinter import Widget
from django.forms import ModelForm
from gestorapp.models import Alumno, Maestro, Tutorias
from django import forms
from django.contrib.admin import widgets
class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class MaestroForm(ModelForm):
    class Meta:
        model = Maestro
        fields = '__all__'

class TutoriasForm(ModelForm):
    class Meta:
        model = Tutorias
        fields = '__all__'

