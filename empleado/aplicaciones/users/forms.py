from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate


# Formulario de registro de usuario
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

# Formulario de inicio de sesión
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña')
            
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        return cleaned_data


