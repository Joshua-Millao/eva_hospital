from django.shortcuts import render,redirect, get_object_or_404
from django.db import IntegrityError
from .models import Paciente
from .models import FichaMedica
from .models import Medico
from .models import Hospital

from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# Create your views here.

# ==========================================
# 1. VISTA DE INICIO (DASHBOARD)
# ==========================================

def login_pagina(request):

    return render(request, 'hospitalapp/login.html')


def dashboard(request):
    total_pacientes = Paciente.objects.count()
    total_fichas = FichaMedica.objects.count()

    contexto = {
        "total_pacientes" : total_pacientes,
        "total_fichas" : total_fichas
    }
    return render(request, "hospitalapp/dashboard.html", contexto)


# ==========================================
# 2. CRUD DE PACIENTES
# ==========================================

# READ: Listar todos los registros
def listar_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, "hospitalapp/listar_paciente.html", {"pacientes" : pacientes})

def detalle_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    return render(request, 'hospitalapp/detalle_paciente.html', {"paciente" : paciente})

# CREATE: Formulario para agregar un nuevo paciente
def crear_paciente(request):

    if request.method == "POST":

        rut_actual =  request.POST.get("rut")
        if Paciente.objects.filter(rut=rut_actual).exists() == True:
            return render(request, "hospitalapp/crear_paciente.html", {
                'error_detectado' : 1})

        Paciente.objects.create(
            rut = rut_actual,
            nombre = request.POST.get("nombre"),
            fecha_nacimiento = request.POST.get("fecha_nacim"),
            direccion = request.POST.get("direccion"),
            telefono = request.POST.get("telefono"),
            # id_paciente =  request.POST.get("id_paciente"),
            prevision =request.POST.get("prevision"),
            # grupo_sanguineo = request.POST.get("grupo_sanguineo")
        )
        return redirect("listar_paciente")
        
    return render(request, "hospitalapp/crear_paciente.html", {
        'error_detectado' : 0})


# UPDATE: Formulario para editar un paciente ya existente
def editar_paciente(request, id):

    # paciente = get_list_or_404(Paciente, id=id)
    paciente = Paciente.objects.get(id=id)

    if request.method == "POST":

        rut_actual =  request.POST.get("rut")
        nombre_actual = request.POST.get("nombre")
        direccion_actual = request.POST.get("direccion")
        telefono_actual = request.POST.get("telefono")

        if paciente.rut == rut_actual:
            return render(request, "hospitalapp/editar_paciente.html", {
                'paciente' : paciente,
                'error_detectado' : 2
                })
        
        if Paciente.objects.filter(rut=rut_actual).exists() == True:
            return render(request, "hospitalapp/editar_paciente.html", {
                'paciente' : paciente,
                'error_detectado' : 1
                })
        
        if rut_actual != "":
            paciente.rut = rut_actual
        if nombre_actual != "":
            paciente.nombre = nombre_actual 
        if direccion_actual != "":
            paciente.direccion = direccion_actual 
        if telefono_actual != "":
            paciente.telefono = telefono_actual

        paciente.fecha_nacimiento = request.POST.get("fecha_nacim")
        paciente.prevision = request.POST.get("prevision")
        paciente.save()

        return redirect("listar_paciente")
    
    return render(request, 'hospitalapp/editar_paciente.html', {
        'paciente' : paciente,
        'error_detectado' : 0
        })


# DELETE: Confirmar y Eliminar
def eliminar_paciente(request, id):
    paciente_eliminar = Paciente.objects.get(id=id)

    if request.method == 'POST':
        paciente_eliminar.delete()

        return redirect('listar_paciente')

    return render(request, 'hospitalapp/eliminar_paciente.html', {
        'paciente': paciente_eliminar
    })


# Integracion de la Api
class LoginAPIView(APIView):

    permission_classes =[AllowAny]

    def post(self, request):

        #Recibir las credenciales desde el JSON
        username = request.data.get('username')
        password = request.data.get('password')

        #Validar las credenciales de usuarios

        usuario = authenticate(
            username=username,
            password=password
        )

        if usuario is not None:

            token, creado = Token.objects.get_or_create(
                user=usuario
            )

            return Response({
                'mensaje': 'Autenticacion correcta',
                'usuario': usuario.username,
                'token':token.key
            }, status=status.HTTP_200_OK)
        return Response({
            'error': 'Usuario o contraseña incorrecta'
        }, status=status.HTTP_401_UNAUTHORIZED)

class hospitalApiView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # GET lista todas las tareas

    def get(self, request):

        paceinte = Paciente.objects.all()

        datos = []

        for paciente in paciente:
            datos.append({
                'rut': paciente.rut,
                'nombre': paciente.nombre,
                'fecha_nacimiento': paciente.fecha_nacimiento,
                'direccion': paciente.direccion,
                'telefono': paciente.telefono,
                'prevision': paciente.prevision
            })
        return Response(datos, status.HTTP_200_OK)

    def post(self, request):

        rut = request.data.get('rut')
        nombre = request.data.get('nombre')
        fecha_nacimiento = request.data.get('fecha_nacimiento')
        direccion = request.data.get('direccion')
        telefono = request.data.get('telefono')
        prevision = request.data.get('prevision')

        # Validar que los campos obligatorios tengan datos

        if not rut or not nombre or not fecha_nacimiento or not direccion or not telefono:
            return Response({
                'error':'El rut, el nombre y fecha de nacimiento, direccion y telefono son obligatorias.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Crear y guardar el paciente enla BD

        paciente = Paciente.objects.create(
            rut = rut,
            nombre = nombre,
            fecha_nacimiento = fecha_nacimiento,
            direccion = direccion,
            telefono = telefono,
            prevision = prevision
        )

        # Devolver el paciente creado

        return Response({
            'Mensaje':'Paciente creado correctamente',
            'Paciente':{
                'rut': paciente.rut,
                'nombre': paciente.nombre,
                'fecha_nacimiento': paciente.fecha_nacimiento,
                'direccion': paciente.direccion,
                'telefono': paciente.telefono,
                'prevision': paciente.prevision
            }
        }, status=status.HTTP_201_CREATED)


class hospitalDetalleApiView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Get: Consultar un paciente por id
    def get(self, request, id):
        paciente = get_object_or_404(Paciente, id=id)

        return Response({
            'id': paciente.id,
            'rut': paciente.rut,
            'nombre': paciente.nombre,
            'fecha_nacimiento': paciente.fecha_nacimiento,
            'direccion': paciente.direccion,
            'telefono': paciente.telefono,
            'prevision': paciente.prevision
        }, status=status.HTTP_200_OK)

    #Delete: Eliminar un paciente
    def delete(self, request, id):
        paciente = get_object_or_404(Paciente, id=id)
        paciente.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)