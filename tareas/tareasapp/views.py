from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def inicio(request):
    paciente_lista = Paciente.objects.all()

    return render(request, 'inicio.html', {
        'pacientes' : paciente_lista
    })

def agregar_paciente(request):

    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        fecha_nacimiento = request.POST['fecha_nacim']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        prevision = request.POST['prevision']

        Paciente.objects.create(
            rut = rut,
            nombre = nombre,
            fecha_nacimiento = fecha_nacimiento,
            direccion = direccion,
            telefono = telefono,
            prevision = prevision
        )

        return redirect('inicio')

    return render(request, 'agregar_paciente.html')

def detalle_paciente(request):
    pass

def modificar_paciente(request):
    pass

# def pagina_test(request):

#     return render(request, 'test.html')
#     pass

# ESTO TMBN ES TEMPORAL HRMNO
# ASLKDNASLJD