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
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departamentos')
    nombre_departamento = models.CharField(max_length=100)
    director_medico = models.OneToOneField(
        Medico, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='departamento_dirigido'
    )

class FichaMedica(models.Model):
    ESTADO_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('EN_CURSO', 'En curso'),
        ('FINALIZADA', 'Finalizada'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='AGENDADA')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='fichas_atendidas')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='fichas_medicas')
    
    motivo_consulta = models.TextField()
    alergias_registradas = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    tratamiento = models.TextField(blank=True, null=True)
    medicamentos_recetados = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ficha {self.id} - {self.paciente.nombre} con Dr. {self.medico.nombre}"