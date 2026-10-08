from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listar_paciente/', views.listar_paciente, name='listar_paciente'),
    path('crear_paciente/', views.crear_paciente, name='crear_paciente'),
    path('eliminar_paciente/<int:id>', views.eliminar_paciente, name='eliminar_paciente'),
    # path('', views.inicio, name='inicio'),
    # path('', views.inicio, name='inicio'),
]