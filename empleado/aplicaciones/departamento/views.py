from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
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
    success_url = reverse_lazy('departamento_app:lista_departamento')

    def form_valid(self, form):
        # Crear el departamento con los datos del formulario
        Departamento.objects.create(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shortName']
        )
        return super().form_valid(form)

class DeleteDepartamentoViews(DeleteView):
    model = Departamento
    template_name = 'departamento/delete.html'
    success_url = reverse_lazy('departamento_app:lista_departamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamento'] = Departamento.objects.get(id=self.kwargs['pk'])
        return context
