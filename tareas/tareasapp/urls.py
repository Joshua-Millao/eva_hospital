from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('test', views.pagina_test, name='test'),
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('eliminar_paciente/<int:id>', views.eliminar_paciente, name='eliminar_paciente'),
    # path('', views.inicio, name='inicio'),
]