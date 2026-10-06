from django.db import models
# Create your models here.
class Persona(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    class Meta:
        abstract = True

class Hospital(models.Model):
    nombre = models.CharField(max_length=100)

class Empleado(Persona):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='empleados')
    id_empleado = models.CharField(max_length=20, unique=True)
    turno = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

class Paciente(Persona):
    prevision = models.TextField()

class Medico(models.Model):
    especialidad = models.TextField()
    numcolegiatura = models.CharField(max_length=50, unique=True)

class Departamento(models.Model):
    pass

class FichaMedica(models.Model):
    fechaHora = models.CharField(max_length=100)
    estado = models.TextField()
    diagnostico = models.CharField(max_length=300)
    tratamiento = models.CharField(max_length=300)