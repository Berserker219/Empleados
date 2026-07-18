from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta, date
from .models import Vacaciones, Permiso, Asistencia, Solicitud, Certificado, Beneficio
from aplicaciones.empleados.models import Empleado

class GeneralViews(TemplateView):
    template_name = 'recursos_humanos/general.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().date()
        
        # 1. Resumen de solicitudes pendientes
        solicitudes_vacaciones_pendientes = Solicitud.objects.filter(
            tipo='vacaciones', 
            estado='pendiente'
        ).count()
        
        solicitudes_permisos_pendientes = Solicitud.objects.filter(
            tipo='permiso', 
            estado='pendiente'
        ).count()
        
        solicitudes_documentos_pendientes = Solicitud.objects.filter(
            tipo='certificado', 
            estado='pendiente'
        ).count()
        
        # 2. Próximos cumpleaños (próximos 7 días)
        proxima_semana = hoy + timedelta(days=7)
        cumpleaneros_semana = Empleado.objects.filter(
            fecha_nacimiento__month=hoy.month,
            fecha_nacimiento__day__gte=hoy.day,
            fecha_nacimiento__day__lte=proxima_semana.day
        ) | Empleado.objects.filter(
            fecha_nacimiento__month=proxima_semana.month,
            fecha_nacimiento__day__lte=proxima_semana.day
        )
        
        # 3. Últimas liquidaciones (últimas 5 solicitudes de tipo liquidación o salida)
        ultimas_liquidaciones = Solicitud.objects.filter(
            tipo__icontains='liquidacion'
        ).order_by('-fecha_solicitud')[:5]
        
        # 4. Indicadores clave
        empleados_activos = Empleado.objects.filter(activo=True).count()
        solicitudes_aprobadas_mes = Solicitud.objects.filter(
            estado='aprobado',
            fecha_solicitud__month=hoy.month,
            fecha_solicitud__year=hoy.year
        ).count()
        vacaciones_pendientes = Vacaciones.objects.filter(aprobado=False).count()
        permisos_activos = Permiso.objects.filter(
            aprobado=True,
            fecha_inicio__lte=hoy,
            fecha_fin__gte=hoy
        ).count()
        
        context.update({
            'solicitudes_vacaciones_pendientes': solicitudes_vacaciones_pendientes,
            'solicitudes_permisos_pendientes': solicitudes_permisos_pendientes,
            'solicitudes_documentos_pendientes': solicitudes_documentos_pendientes,
            'cumpleaneros_semana': cumpleaneros_semana,
            'ultimas_liquidaciones': ultimas_liquidaciones,
            'empleados_activos': empleados_activos,
            'solicitudes_aprobadas_mes': solicitudes_aprobadas_mes,
            'vacaciones_pendientes': vacaciones_pendientes,
            'permisos_activos': permisos_activos,
        })
        
        return context

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
