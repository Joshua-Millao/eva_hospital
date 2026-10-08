from django.shortcuts import render,redirect, get_list_or_404
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
    paciente = Paciente.objects.all()
    return render(request, "listar_paciente.html", {"paciente" : paciente})


# CREATE: Formulario para agregar un nuevo paciente
def crear_paciente(request):
    if request.method == "POST":
        Paciente.objects.create(
            rut = request.POST.get("rut"),
            nombre = request.POST.get("nombre"),
            fecha_nacimiento = request.POST.get("fecha_nacimiento"),
            direccion = request.POST.get("direccion"),
            telefono = request.POST.get("telefono"),
            id_paciente =  request.POST.get("id_paciente"),
            prevision =request.POST.get("prevision"),
            grupo_sanguineo = request.POST.get("grupo_sanguineo")
        )
        return redirect("listar_paciente.html")
    
    return render(request, "crear_paciente.html")


# UPDATE: Formulario para editar un paciente ya existente
def editar_paceinte(request):
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
        return redirect("listar_paciente.html")
    return render(request, 'editar_paciente.html', {'paciente' : paciente})


# DELETE: Confirmar y Eliminar
def eliminar_paciente(request, id):
    paciente_eliminar = Paciente.objects.get(id=id)

    if request.method == 'POST':
        paciente_eliminar.delete()

        return redirect('inicio')

    return render(request, 'eliminar_paciente.html', {
        'paciente': paciente_eliminar
    })