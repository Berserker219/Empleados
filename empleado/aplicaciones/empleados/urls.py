from django.contrib import admin
from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path('', views.InicioViews.as_view(), name='inicio'),
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('area/<name>/', views.ListByAreaEmpleado.as_view(),name='area_empleado'),
    path('lista-empleados-admin/', views.ListEmpleadosAdmin.as_view(),name='empleados_admin'),
    path('buscar_empleado/', views.ListEmpleadosByKword.as_view(),name='lista'),
    path('listar_habilidades_empleado/',views.ListHabilidadesEmpleado.as_view()),
    path('ver_empleado/<pk>/', views.EmpleadoDetailViews.as_view(), name='detalle_empleado'),
    path('add_empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccesView.as_view(), name='correcto'),
    path('update_empleado/<pk>/',views.EmpleadoUpdateView.as_view(),name='modificar_empleado'),
    path('delete_empleado/<pk>/', views.EmpleadoDeleteView.as_view(),name='borrado'),
    
]