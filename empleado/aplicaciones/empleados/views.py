from django.shortcuts import render
from django.views.generic import ListView
from .models import Empleado


class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    model = Empleado
    context_object_name = "lista"

class ListByAreaEmpleado(ListView):
    template_name = 'empleados/list_all.html'
    model = Empleado