from django.urls import path

from BibliotecaApp import views



urlpatterns = [
   
    path('',views.home, name="Home"),
    
]