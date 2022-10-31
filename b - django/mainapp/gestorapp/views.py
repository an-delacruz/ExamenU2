from django.shortcuts import render, get_object_or_404, redirect
from gestorapp.models import Alumno, Maestro, Tutorias
from gestorapp.forms import AlumnoForm, MaestroForm, TutoriasForm
# Create your views here.

def alumno(request):
        alumno = Alumno.objects.order_by('id')
        return render(request,'alumno.html',{'Alumno':alumno})

def detallealumno(request,id):
        alumno = get_object_or_404(Alumno, pk=id)
        return render(request,'detallealumno.html',{'alumno':alumno})

def agregaralumno(request):
        if request.method=="POST":
                formaAlumno = AlumnoForm(request.POST)
                if formaAlumno.is_valid():
                        formaAlumno.save()
                        return redirect('alumno')
        else:
                formaAlumno = AlumnoForm()
                return render(request, 'agregaralumno.html', {'formaAlumno':formaAlumno})

def editaralumno(request, id):
        alumno = get_object_or_404(Alumno, pk=id)#se busca nmediante el id
        if request.method=="POST":
                formaAlumno = AlumnoForm(request.POST,instance=alumno)#objeto que ya existe, y si existe cuales son los valores
                if formaAlumno.is_valid():
                        formaAlumno.save()
                        return redirect('alumno')
        else:
                formaAlumno = AlumnoForm(instance=alumno)
                return render(request, 'editaralumno.html', {'formaAlumno':formaAlumno})

def eliminaralumno(request, id):
        alumno = get_object_or_404(Alumno, pk=id)#se busca nmediante el id
        if alumno:
                alumno.delete()
        return redirect('alumno')

#MAESTRO
def maestro(request):
        maestro = Maestro.objects.order_by('id')
        return render(request,'maestro.html',{'Maestro':maestro})

def detallemaestro(request,id):
        maestro = get_object_or_404(Maestro, pk=id)
        return render(request,'detallemaestro.html',{'maestro':maestro})

def agregarmaestro(request):
        if request.method=="POST":
                formaMaestro = MaestroForm(request.POST)
                if formaMaestro.is_valid():
                        formaMaestro.save()
                        return redirect('maestro')
        else:
                formaMaestro = MaestroForm()
                return render(request, 'agregarmaestro.html', {'formaMaestro':formaMaestro})

def editarmaestro(request, id):
        maestro = get_object_or_404(Maestro, pk=id)#se busca nmediante el id
        if request.method=="POST":
                formaMaestro = MaestroForm(request.POST,instance=maestro)#objeto que ya existe, y si existe cuales son los valores
                if formaMaestro.is_valid():
                        formaMaestro.save()
                        return redirect('maestro')
        else:
                formaMaestro = MaestroForm(instance=maestro)
                return render(request, 'editarmaestro.html', {'formaMaestro':formaMaestro})

def eliminarmaestro(request, id):
        maestro = get_object_or_404(Maestro, pk=id)#se busca nmediante el id
        if maestro:
                maestro.delete()
        return redirect('maestro')


#TUTORIAS
def tutoria(request):
        tutorias = Tutorias.objects.order_by('id')
        return render(request,'tutorias.html',{'Tutorias':tutorias})


def detalletutoria(request,id):
        tutoria = get_object_or_404(Tutorias, pk=id)
        return render(request,'detalletutorias.html',{'tutoria':tutoria})

def agregartutoria(request):
        if request.method=="POST":
                formaTutorias = TutoriasForm(request.POST)
                if formaTutorias.is_valid():
                        formaTutorias.save()
                        return redirect('tutoria')
        else:
                formaTutorias = TutoriasForm()
                return render(request, 'agregartutorias.html', {'formaTutorias':formaTutorias})

def editartutoria(request, id):
        tutoria = get_object_or_404(Tutorias, pk=id)#se busca nmediante el id
        if request.method=="POST":
                formaTutorias = TutoriasForm(request.POST,instance=tutoria)#objeto que ya existe, y si existe cuales son los valores
                if formaTutorias.is_valid():
                        formaTutorias.save()
                        return redirect('tutoria')
        else:
                formaTutorias = TutoriasForm(instance=tutoria)
                return render(request, 'editartutorias.html', {'formaTutorias':formaTutorias})

def eliminartutorias(request, id):
        tutoria = get_object_or_404(Tutorias, pk=id)#se busca nmediante el id
        if tutoria:
                tutoria.delete()
        return redirect('tutoria')

