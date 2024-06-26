from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from aplicaciones.empleados.models import Empleado 
from .models import Departamento
from .forms import NewDepartamentoFomrs


class ListaDepartamento(ListView):
    model= Departamento
    template_name = 'departamento/lista_departamento.html'
    context_object_name = 'lista_depa'
    

class NewDepartamentoViews(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoFomrs
    success_url = '/'

    def form_valid(self, form):
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shortName']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name= nombre,
            last_name = apellido,
            job = '1',
            departamento=depa,
        )
        return super(NewDepartamentoViews,self).form_valid(form)

    
    