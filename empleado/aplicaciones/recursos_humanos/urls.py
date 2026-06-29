from django.urls import path
from .views import (
    VacacionesListView, VacacionesDetailView,
    SolicitudCreateView,
    PermisoListView,
    AsistenciaListView
)

urlpatterns = [
    path("vacaciones/", VacacionesListView.as_view(), name="vacaciones_list"),
    path("vacaciones/<int:pk>/", VacacionesDetailView.as_view(), name="vacaciones_detail"),
    path("solicitudes/nueva/", SolicitudCreateView.as_view(), name="solicitud_create"),
    path("permisos/", PermisoListView.as_view(), name="permisos_list"),
    path("asistencia/", AsistenciaListView.as_view(), name="asistencia_list"),
]
