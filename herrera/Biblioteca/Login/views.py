from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la página deseada después de iniciar sesión exitosamente
        else:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect('index')
            except User.DoesNotExist:
                pass

            error_message = 'Credenciales inválidas. Inténtalo de nuevo.'
            messages.error(request, error_message)

    return render(request, 'login.html')


def logout_view(request):
    """
    La función cierra la sesión del usuario y lo redirige a la página de inicio de sesión.
    
    :param request: el objeto de solicitud representa la solicitud HTTP actual. Contiene información
    sobre la solicitud, como el usuario que realiza la solicitud, el método HTTP utilizado y cualquier dato enviado con
    la solicitud
    :return: una respuesta de redireccionamiento a la página de 'inicio de sesión'.
    """
    logout(request)

    # Redirige a la página de inicio o a donde desees que vaya después de cerrar sesión
    return redirect('index')


from django.contrib.auth.models import User

# ...

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifica si el usuario ya existe
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'El nombre de usuario ya está en uso.'})

        # Crea el nuevo usuario
        user = User.objects.create_user(username=username, password=password)
        user.is_superuser = request.POST.get('is_superuser') == 'true'
        user.is_staff = user.is_superuser  # Asigna el permiso de staff al superusuario
        user.save()

        # Inicia sesión automáticamente
        login(request, user)

        # Redirige al index después del registro exitoso
       
        return redirect('index')

    return render(request, 'register.html', {'error_message': ''})