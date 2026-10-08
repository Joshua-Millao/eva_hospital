from django.shortcuts import render,redirect, get_list_or_404
from django.db import IntegrityError
from .models import Paciente
from .models import FichaMedica
from .models import Medico

# Create your views here.

# ==========================================
# 1. VISTA DE INICIO (DASHBOARD)
# ==========================================

def inicio(request):
    total_pacientes = Paciente.objects.count()
    total_fichas = FichaMedica.objects.count()

    contexto = {
        "total_pacientes" : total_pacientes,
        "total_fichas" : total_fichas
    }
    return render(request, "inicio.html", contexto)


# ==========================================
# 2. CRUD DE PACIENTES
# ==========================================

# READ: Listar todos los registros
def listar_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, "listar_paciente.html", {"pacientes" : pacientes})


# CREATE: Formulario para agregar un nuevo paciente
def crear_paciente(request):

    rut_actual =  request.POST.get("rut")

    if request.method == "POST":

        if Paciente.objects.filter(rut=rut_actual).exists() == False:
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
        else:
            return render(request, "crear_paciente.html", {
                'error_detectado' : 1
            })
    
    return render(request, "crear_paciente.html", {
        'error_detectado' : 0
    })


# UPDATE: Formulario para editar un paciente ya existente
def editar_paciente(request):
    paciente = get_list_or_404(Paciente, id=id)

    if request.method == "POST":
        paciente.rut = request.POST.get("rut"),
        paciente.nombre = request.POST.get("nombre"),
        paciente.fecha_nacimiento = request.POST.get("fecha_nacimiento"),
        paciente.direccion = request.POST.get("direccion"),
        paciente.telefono = request.POST.get("telefono"),
        paciente.id_paciente = request.POST.get("id_paciente"),
        paciente.prevision = request.POST.get("prevision"),
        paciente.grupo_sanguineo = request.POST.get("grupo_sanguineo")
        paciente.save()
        return redirect("listar_paciente")
    return render(request, 'editar_paciente.html', {'paciente' : paciente})


# DELETE: Confirmar y Eliminar
def eliminar_paciente(request, id):
    paciente_eliminar = Paciente.objects.get(id=id)

    if request.method == 'POST':
        paciente_eliminar.delete()

        return redirect('listar_paciente')

    return render(request, 'eliminar_paciente.html', {
        'paciente': paciente_eliminar
    })