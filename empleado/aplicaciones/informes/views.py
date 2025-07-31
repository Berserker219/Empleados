from django.shortcuts import render
from django.db.models import Count, Avg, F, ExpressionWrapper, FloatField, Case, When, Value, CharField
from django.db.models import IntegerField
from datetime import date
from aplicaciones.empleados.models import Empleado
import json

def dashboard_general(request):
    try:
        # 1. Empleados por departamento
        empleados_dep = Empleado.objects.filter(
            departamento__isnull=False
        ).values(
            'departamento__name'
        ).annotate(
            total=Count('id')
        ).order_by('-total')

        # 2. Distribución por género
        genero_dist = Empleado.objects.exclude(
            genero__exact=''
        ).values(
            'genero'
        ).annotate(
            total=Count('id')
        ).order_by('-total')

        # 3. Salario promedio por departamento
        salario_prom = Empleado.objects.filter(
            departamento__isnull=False,
            salario__isnull=False
        ).values(
            'departamento__name'
        ).annotate(
            promedio=Avg('salario')
        ).order_by('-promedio')

        # 4. Antigüedad de empleados (rangos)
        
        antiguedad = Empleado.objects.exclude(
            fecha_contratacion__isnull=True
        ).annotate(
            antiguedad_dias=ExpressionWrapper(
                date.today() - F('fecha_contratacion'),
                output_field=IntegerField()
            )
        ).annotate(
            rango=Case(
                When(antiguedad_dias__lt=365, then=Value('Menos de 1 año')),
                When(antiguedad_dias__gte=365, antiguedad_dias__lt=1095, then=Value('1-2 años')),
                When(antiguedad_dias__gte=1095, antiguedad_dias__lt=1825, then=Value('3-4 años')),
                When(antiguedad_dias__gte=1825, then=Value('5+ años')),
                default=Value('Sin fecha'),
                output_field=CharField()
            )
        ).values(
            'rango'
        ).annotate(
            total=Count('id')
        ).order_by('rango')

        context = {
            # Gráfica 1
            'departamentos': json.dumps([d['departamento__name'] for d in empleados_dep]),
            'conteo_dep': json.dumps([d['total'] for d in empleados_dep]),
            
            # Gráfica 2
            'generos': json.dumps([g['genero'] for g in genero_dist]),
            'conteo_genero': json.dumps([g['total'] for g in genero_dist]),
            
            # Gráfica 3
            'deptos_salario': json.dumps([s['departamento__name'] for s in salario_prom]),
            'salarios_prom': json.dumps([float(s['promedio']) for s in salario_prom]),
            
            # Gráfica 4
            'rangos_antiguedad': json.dumps([a['rango'] for a in antiguedad]),
            'conteo_antiguedad': json.dumps([a['total'] for a in antiguedad])
        }
        
        return render(request, 'informes/dashboard_general.html', context)
        
    except Exception as e:
        print(f"Error en dashboard: {str(e)}")
        return render(request, 'informes/dashboard_general.html', {
            'departamentos': '[]',
            'conteo_dep': '[]',
            'generos': '[]',
            'conteo_genero': '[]',
            'deptos_salario': '[]',
            'salarios_prom': '[]',
            'rangos_antiguedad': '[]',
            'conteo_antiguedad': '[]'
        })