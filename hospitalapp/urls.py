from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_pagina, name= 'login_pagina'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('listar_paciente/', views.listar_paciente, name='listar_paciente'),
    path('crear_paciente/', views.crear_paciente, name='crear_paciente'),
    path('eliminar_paciente/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('editar_paciente/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('detalle_paciente/<int:id>/', views.detalle_paciente, name='detalle_paciente'),
    path('api/login/', views.LoginAPIView.as_view(), name='login_api'),
    path('api/hospital/',views.hospitalApiView.as_view(), name='api_hospital'),
    path('api/hospital/<int:id>/',views.hospitalDetalleApiView.as_view(), name='api_hospital_Detalle')
]