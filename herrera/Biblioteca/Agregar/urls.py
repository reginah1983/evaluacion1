from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.add, name="add"),
    path('editar/<int:libro_id>/',views.editar, name="editar"),
    path('eliminar/<int:libro_id>/', views.cambiarEstado, name="eliminar") ,
    path('buscar/', views.buscar, name='buscar'),
]
