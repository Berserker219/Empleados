from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, DetailView, CreateView, TemplateView
from aplicaciones.departamento.models import Departamento
from .forms import EmpleadoForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

# models
from .models import Empleado
# forms
from .forms import EmpleadoForm

# Vista que ccarga la pagina de inicio
class InicioViews(TemplateView):
    template_name = 'inicio.html'

# Lista de todos los Empleados
class ListAllEmpleados(LoginRequiredMixin,ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'lista_empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        print(f"Palabra clave recibida: {palabra_clave}")
        lista =  Empleado.objects.filter(
            full_name__icontains=palabra_clave
        ).order_by('first_name')
        print(f"Resultados encontrados: {lista.count()}")
        return lista
    

# Lista de todos los Empleados en Admin
class ListEmpleadosAdmin(LoginRequiredMixin,ListView):
    template_name = 'empleados/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleadosAdmin'
    model = Empleado

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        print(f"Palabra clave recibida: {palabra_clave}")
        lista =  Empleado.objects.filter(
            full_name__icontains=palabra_clave
        ).order_by('first_name')
        print(f"Resultados encontrados: {lista.count()}")
        return lista

# Lista de Empleados por Area
class ListByAreaEmpleado(LoginRequiredMixin,ListView):
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleado'

    def get_queryset(self):
        area = self.kwargs['name']
        lista =  Empleado.objects.filter(
            departamento__name=area
        )
        return lista


# Busqueda de Empleados
class ListEmpleadosByKword(LoginRequiredMixin,ListView):
    template_name = 'empleados/by_kword.html'
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista =  Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

# Habilidades de Empleado
class ListHabilidadesEmpleado(LoginRequiredMixin,ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = "habilidades"

    def get_queryset(self):
        empleado = Empleado.objects.get(id=6)
        return empleado.habilidades.all()

# Detalles de Empleado
class EmpleadoDetailViews(LoginRequiredMixin,DetailView):
    model = Empleado
    template_name = 'empleados/detail_empleado.html'
    context_object_name = 'detalle'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailViews, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    

class SuccesView(LoginRequiredMixin,TemplateView):
    template_name = "empleados/success.html"

# Crear Empleado
class EmpleadoCreateView(LoginRequiredMixin,CreateView):
    template_name = 'empleados/add.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def form_valid(self, form):
        
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

    
# Actualizar empleado
class EmpleadoUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "empleados/update.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)

# Elimar empleado
class EmpleadoDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'empleados/delete.html'
    model = Empleado
    success_url = reverse_lazy('empleados_app:empleados_admin')

