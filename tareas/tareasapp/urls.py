from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    # path('', views.inicio, name='inicio'),
]