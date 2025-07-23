import json
from django.shortcuts import render
from aplicaciones.empleados.models import Empleado
from aplicaciones.departamento.models import Departamento
from django.db.models import Count

# esta funcione es para mostrar los dashboard
def dashboard_general(request):
    empleados_por_depa = Departamento.objects.annotate(total=Count('empleado'))
    labels = [d.name for d in empleados_por_depa]
    valores = [d.total for d in empleados_por_depa]

    context = {
        'labels': json.dumps(labels),
        'valores': json.dumps(valores),
        'total_empleados': Empleado.objects.count(),
        'total_departamentos': Departamento.objects.count(),
    }
    return render(request, 'informes/dashboard_general.html', context)
