from django.urls import path
from LibrosApp  import views


urlpatterns = [
    path('',views.index, name="index"),
    path('<int:id>', views.view_producto, name="view_producto"),
    
]
