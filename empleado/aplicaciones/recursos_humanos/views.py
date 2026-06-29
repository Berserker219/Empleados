from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Vacaciones, Permiso, Asistencia, Solicitud, Certificado, Beneficio

# Listar vacaciones
class VacacionesListView(ListView):
    model = Vacaciones
    template_name = "recursos_humanos/vacaciones_list.html"
    context_object_name = "vacaciones"

# Detalle de vacaciones
class VacacionesDetailView(DetailView):
    model = Vacaciones
    template_name = "recursos_humanos/vacaciones_detail.html"
    context_object_name = "vacacion"

# Crear solicitud genérica
class SolicitudCreateView(CreateView):
    model = Solicitud
    fields = ["tipo", "descripcion"]
    template_name = "recursos_humanos/solicitud_form.html"
    success_url = reverse_lazy("solicitudes_list")

# Listar permisos
class PermisoListView(ListView):
    model = Permiso
    template_name = "recursos_humanos/permisos_list.html"
    context_object_name = "permisos"

# Listar asistencia
class AsistenciaListView(ListView):
    model = Asistencia
    template_name = "recursos_humanos/asistencia_list.html"
    context_object_name = "asistencias"
