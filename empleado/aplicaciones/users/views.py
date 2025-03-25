from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  CreateView, FormView, RedirectView
from django.contrib.auth import login, authenticate, logout
# formularios    
from .forms import CustomUserCreationForm, LoginForm



class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('empleados_app:inicio')  # Redirige a la página de inicio después del registro

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object  # El usuario recién creado
        login(self.request, user)  # Inicia sesión automáticamente después del registro
        return response
    


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('empleados_app:inicio')  # Redirige a la página de inicio después del login

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    

class LogoutView(RedirectView):
    url = reverse_lazy('empleados_app:inicio')  # Redirige a la página de inicio después del logout
    redirect_authenticated_user = True  # Redirige al usuario a la página de inicio si ya está autenticado
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
    

