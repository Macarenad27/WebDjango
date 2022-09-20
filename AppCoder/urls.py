from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', index),
    path('cursos2/', cursos2),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('entregables/', entregables),
    path('home/', home)
]