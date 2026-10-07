from django.contrib import admin
from .models import Hospital
from .models import Empleado
from .models import Medico
from .models import Paciente
from .models import Departamento
from .models import FichaMedica

# Register your models here.

admin.site.register(Hospital)
admin.site.register(Empleado)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Departamento)
admin.site.register(FichaMedica)