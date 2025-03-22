from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('new-departamento/', views.NewDepartamentoViews.as_view(), name='nuevo_departamento'),
    path('lista-departamento/', views.ListaDepartamento.as_view(),name='lista_departamento'),
    path('borrar-departamento/<int:pk>/', views.DeleteDepartamentoViews.as_view(), name='borrar_departamento'),
]