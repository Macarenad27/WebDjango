from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

def home(self, name):
    return HttpResponse(f"Hola soy la página {name}")

def index(request):
    return HttpResponse(f"Hola soy la página INICIO")

def homepage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {"nombre": "Maca", "apellido": "Díaz", "lista": lista}
    planilla = loader.get_template("home.html")
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    #planilla = loader.get_template("cursos.html")
    curso = Curso(nombre="python", camada=23800)
    curso.save()
    documento = f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse(documento)


