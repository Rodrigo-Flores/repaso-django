from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehiculo, Persona


def inventario(request):
    return render(request, 'base.html', context={'nombre': [1, 2, 3]})


def ejecutar(request):
    auto = Vehiculo.objects.get(pk=1)

    personas = Persona.objects.all()

    datos = {
        'nombre': 'rodrigo',
        'edad': 21,
        'canciones': ['primera', 'segunda', 'tercera'],
        'frutas': [
            'pera',
            'manzana',
            'pera',
            'naranja',
            'mango',
            'pera',
            'frutilla',
        ],
        'contador': 0,
        'auto': auto,
        'personas': personas,
    }

    return render(request, 'primero.html', context=datos)
