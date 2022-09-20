from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estudiante
from AppCoder.forms import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def cursos2(request):
    return render(request, "cursos2.html")

def profesores(request):
    return render(request, "profesores.html")

def estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email=request.POST['email'])
        estudiante.save()
        return render(request, "home.html")
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")


def api_estudiantes(request):
    if request.method == "POST":
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            estudiante = Estudiante(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            estudiante.save()
            return render(request, "api_estudiantes.html")
    else:
        formulario = form_estudiantes()
    return render(request, "api_estudiantes.html", {"formulario": formulario})
    