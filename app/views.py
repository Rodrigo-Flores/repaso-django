from django.shortcuts import render
from django.http import HttpResponse

def inventario(request):
    return HttpResponse("<h1>COCA COLA</h1>")

def preguntas(request):
    return HttpResponse('<h1 style="color: blue;">¿QUÉ?</h1>')

def preguntas_con_template(request):
    return render(request, 'preguntas.html')