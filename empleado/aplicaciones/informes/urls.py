from django.urls import path
from . import views

app_name = 'informes'

urlpatterns = [
    path('', views.dashboard_general, name='dashboard_general'),
]
