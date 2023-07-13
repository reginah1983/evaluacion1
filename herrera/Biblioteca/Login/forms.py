from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_superuser:
            raise forms.ValidationError(
                "Ingreso no permitido. Por favor, inicie sesión con una cuenta de superusuario."
            )