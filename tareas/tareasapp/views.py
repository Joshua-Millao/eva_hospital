from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def inicio(request):
    paciente_lista = Paciente.objects.all()

    return render(request, 'inicio.html', {
        'pacientes' : len(paciente_lista)
    })

# ESTO TMBN ES TEMPORAL HRMNO
# ASLKDNASLJD