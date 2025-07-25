import os
import pandas as pd
import matplotlib.pyplot as plt
from django.conf import settings
from aplicaciones.empleados.models import Empleado

def generar_grafica_empleados_por_departamento():
    # Obtener los datos
    empleados = Empleado.objects.select_related('departamento').values('departamento__name')
    df = pd.DataFrame(empleados)

    # Verificar que hay datos
    if df.empty or 'departamento__name' not in df.columns:
        print("⚠️ No hay empleados registrados o falta la columna de departamento.")
        return

    # Agrupar y contar
    conteo = df['departamento__name'].value_counts()

    # Crear la gráfica
    plt.figure(figsize=(6, 4))
    conteo.plot(kind='bar', color='#3498db')
    plt.title('Empleados por Departamento')
    plt.xlabel('Departamento')
    plt.ylabel('Cantidad')
    plt.tight_layout()

    # Ruta dinámica hacia static/img
    ruta_static_img = os.path.join(settings.BASE_DIR, 'static', 'img')
    os.makedirs(ruta_static_img, exist_ok=True)  # crea carpeta si no existe

    ruta_grafica = os.path.join(ruta_static_img, 'grafica_departamento.png')
    plt.savefig(ruta_grafica)
    plt.close()
