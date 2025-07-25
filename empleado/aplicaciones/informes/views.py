import json
from django.shortcuts import render
from aplicaciones.empleados.models import Empleado
from aplicaciones.departamento.models import Departamento
from django.db.models import Count
from .utils.graficas import generar_grafica_empleados_por_departamento

# esta funcione es para mostrar los dashboard
def dashboard_general(request):
    generar_grafica_empleados_por_departamento()
    context = {
        'grafica_url': '/static/img/grafica_departamento.png',
        # otras métricas que quieras mostrar
    }
    return render(request, 'dashboard_general.html', context)
