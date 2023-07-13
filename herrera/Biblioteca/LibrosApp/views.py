from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import Libros
from django.shortcuts import reverse

# Create your views here.
def index(request):
   
    
    return render(request, 'biblioteca/index.html', {"libro": Libros.objects.all()})

def view_producto(request,id):
    libros = Libros.objects.get(pk=id)
    return HttpResponseRedirect(reverse,('index'))


