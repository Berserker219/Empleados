document.addEventListener("DOMContentLoaded", () => {
  // Navegación lateral
  const menuLinks = document.querySelectorAll(".sidebar-menu a");
  const panels = document.querySelectorAll(".grafica-panel");

  menuLinks.forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault();
      const target = link.getAttribute("data-grafica");

      panels.forEach(panel => {
        panel.classList.remove("active");
      });

      const panelToShow = document.getElementById(`grafica-${target}`);
      if (panelToShow) {
        panelToShow.classList.add("active");
      }
    });
  });

  // Renderizar gráfica general
  const ctx = document.getElementById('graficaEmpleadosPorDepartamento');
  if (ctx) {
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: JSON.parse(window.chartData.labelsGeneral),
        datasets: [{
          label: 'Empleados por Departamento',
          data: JSON.parse(window.chartData.valoresGeneral),
          backgroundColor: '#3498db'
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'bottom' },
          title: { display: true, text: 'Empleados por Departamento' }
        }
      }
    });
  }
});
