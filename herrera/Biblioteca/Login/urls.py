from django.urls import path
from Login.views import login_view,logout_view,register

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/',register , name='registrar'),
]
  
