// // Objeto para almacenar todas las gráficas
// const charts = {
//     mainChart: null,
//     miniCharts: []
// };

// // Función para crear gráficas
// function createChart(ctx, type, labels, data, options = {}) {
//     // Destruir gráfica existente si hay una
//     if (ctx.chart) {
//         ctx.chart.destroy();
//     }
    
//     const defaults = {
//         responsive: true,
//         maintainAspectRatio: false,
//         plugins: {
//             legend: {
//                 position: 'top',
//             }
//         }
//     };
    
//     const finalOptions = {...defaults, ...options};
    
//     ctx.chart = new Chart(ctx, {
//         type: type,
//         data: {
//             labels: labels,
//             datasets: [{
//                 data: data,
//                 backgroundColor: [
//                     'rgba(52, 152, 219, 0.7)',
//                     'rgba(155, 89, 182, 0.7)',
//                     'rgba(26, 188, 156, 0.7)',
//                     'rgba(241, 196, 15, 0.7)',
//                     'rgba(230, 126, 34, 0.7)'
//                 ],
//                 borderColor: [
//                     'rgba(52, 152, 219, 1)',
//                     'rgba(155, 89, 182, 1)',
//                     'rgba(26, 188, 156, 1)',
//                     'rgba(241, 196, 15, 1)',
//                     'rgba(230, 126, 34, 1)'
//                 ],
//                 borderWidth: 1
//             }]
//         },
//         options: finalOptions
//     });
    
//     return ctx.chart;
// }

// // Función para mostrar gráfica principal
// function showMainChart(type, labels, data, options) {
//     const ctx = document.getElementById('mainChart');
//     charts.mainChart = createChart(ctx, type, labels, data, options);
//     ctx.style.display = 'block';
// }

// // Función para cargar todas las mini gráficas
// function loadMiniCharts() {
//     const dataElement = document.getElementById('chartData');
    
//     // Mini gráfica 1: Distribución por género (pastel)
//     const ctx1 = document.getElementById('miniChart1');
//     charts.miniCharts[0] = createChart(ctx1, 'pie', 
//         JSON.parse(dataElement.dataset.generos),
//         JSON.parse(dataElement.dataset.totalGenero),
//         {
//             plugins: {
//                 title: {
//                     display: true,
//                     text: 'Distribución por Género'
//                 }
//             }
//         }
//     );
    
//     // Mini gráfica 2: Salario promedio (barra horizontal)
//     const ctx2 = document.getElementById('miniChart2');
//     charts.miniCharts[1] = createChart(ctx2, 'bar', 
//         JSON.parse(dataElement.dataset.deptosSalario),
//         JSON.parse(dataElement.dataset.salariosPromedio),
//         {
//             indexAxis: 'y',
//             plugins: {
//                 title: {
//                     display: true,
//                     text: 'Salario Promedio'
//                 }
//             },
//             scales: {
//                 x: {
//                     beginAtZero: true
//                 }
//             }
//         }
//     );
    
//     // Mini gráfica 3: Antigüedad (doughnut)
//     const ctx3 = document.getElementById('miniChart3');
//     charts.miniCharts[2] = createChart(ctx3, 'doughnut', 
//         JSON.parse(dataElement.dataset.rangosAntiguedad),
//         JSON.parse(dataElement.dataset.totalAntiguedad),
//         {
//             plugins: {
//                 title: {
//                     display: true,
//                     text: 'Antigüedad'
//                 }
//             }
//         }
//     );
// }

// // Función para cambiar la gráfica principal según selección
// function setupChartSwitcher() {
//     const menuItems = document.querySelectorAll('.menu-lateral a');
//     const dataElement = document.getElementById('chartData');
    
//     menuItems.forEach(item => {
//         item.addEventListener('click', function(e) {
//             e.preventDefault();
            
//             // Actualizar clase active
//             menuItems.forEach(i => i.classList.remove('active'));
//             this.classList.add('active');
            
//             // Obtener datos
//             const chartType = this.dataset.chart;
//             const loader = document.getElementById('chartLoader');
//             loader.style.display = 'flex';
            
//             // Mostrar gráfica correspondiente
//             setTimeout(() => {
//                 try {
//                     switch(chartType) {
//                         case 'empleados-departamento':
//                             showMainChart('bar', 
//                                 JSON.parse(dataElement.dataset.departamentos),
//                                 JSON.parse(dataElement.dataset.cantidades),
//                                 {
//                                     plugins: {
//                                         title: {
//                                             display: true,
//                                             text: 'Empleados por Departamento'
//                                         }
//                                     },
//                                     scales: {
//                                         y: {
//                                             beginAtZero: true,
//                                             ticks: {
//                                                 stepSize: 1,
//                                                 precision: 0
//                                             }
//                                         }
//                                     }
//                                 }
//                             );
//                             break;
                            
//                         case 'distribucion-genero':
//                             showMainChart('pie', 
//                                 JSON.parse(dataElement.dataset.generos),
//                                 JSON.parse(dataElement.dataset.totalGenero),
//                                 {
//                                     plugins: {
//                                         title: {
//                                             display: true,
//                                             text: 'Distribución por Género'
//                                         }
//                                     }
//                                 }
//                             );
//                             break;
                            
//                         // Añade más casos según necesites
//                     }
                    
//                     loader.style.display = 'none';
//                 } catch (error) {
//                     console.error('Error al cambiar gráfica:', error);
//                     loader.style.display = 'none';
//                 }
//             }, 300);
//         });
//     });
// }

// // Función principal de inicialización
// function initDashboard() {
//     const loader = document.getElementById('chartLoader');
    
//     try {
//         // Cargar mini gráficas
//         loadMiniCharts();
        
//         // Configurar switcher de gráficas
//         setupChartSwitcher();
        
//         // Mostrar primera gráfica por defecto
//         const defaultItem = document.querySelector('.menu-lateral a.active');
//         if (defaultItem) {
//             defaultItem.click();
//         } else {
//             document.querySelector('.menu-lateral a').click();
//         }
        
//         loader.style.display = 'none';
//     } catch (error) {
//         console.error('Error al inicializar dashboard:', error);
//         loader.style.display = 'none';
//     }
// }

// // Inicialización condicional
// if (document.getElementById('mainChart')) {
//     document.addEventListener('DOMContentLoaded', initDashboard);
// }

// // script.js - solo se ejecuta si existen los elementos necesarios
// document.addEventListener('DOMContentLoaded', function() {
//     const slides = document.querySelectorAll('.slide');
    
//     // Si no hay slides, salir (para páginas que no usan slideshow)
//     if (slides.length === 0) return;

//     let currentSlide = 0;
    
//     function showSlide(n) {
//         slides.forEach(slide => {
//             slide.style.display = 'none';
//         });
//         currentSlide = (n + slides.length) % slides.length;
//         slides[currentSlide].style.display = 'block';
//     }
    
//     function nextSlide() {
//         showSlide(currentSlide + 1);
//     }
    
//     // Inicializar
//     showSlide(0);
//     setInterval(nextSlide, 3000);
// });



// Configuración inicial
document.addEventListener('DOMContentLoaded', function() {
    // Verificar si estamos en la página correcta
    const mainChart = document.getElementById('mainChart');
    if (!mainChart) return;
    
    try {
        // Obtener elementos del DOM
        const dataElement = document.getElementById('chartData');
        const loader = document.getElementById('chartLoader');
        
        // Verificar que existan los elementos necesarios
        if (!dataElement) {
            throw new Error('No se encontraron los datos para las gráficas');
        }
        
        // Parsear datos
        const data = {
            departamentos: JSON.parse(dataElement.dataset.departamentos),
            conteoDep: JSON.parse(dataElement.dataset.conteoDep),
            generos: JSON.parse(dataElement.dataset.generos),
            conteoGenero: JSON.parse(dataElement.dataset.conteoGenero),
            deptosSalario: JSON.parse(dataElement.dataset.deptosSalario),
            salariosProm: JSON.parse(dataElement.dataset.salariosProm),
            rangosAntiguedad: JSON.parse(dataElement.dataset.rangosAntiguedad),
            conteoAntiguedad: JSON.parse(dataElement.dataset.conteoAntiguedad)
        };
        
        // Inicializar gráficas
        initCharts(data);
        
        // Configurar eventos del menú
        setupMenuEvents(data);
        
        // Ocultar loader
        if (loader) loader.style.display = 'none';
        
    } catch (error) {
        console.error('Error en dashboard:', error);
        showError(error.message);
    }
});

// Función para inicializar todas las gráficas
function initCharts(data) {
    // 1. Gráfica principal (Empleados por departamento)
    createChart('mainChart', {
        type: 'bar',
        labels: data.departamentos,
        data: data.conteoDep,
        label: 'Empleados por Departamento',
        backgroundColor: '#3498db',
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            }
        }
    });
    
    // 2. Gráfica de género
    createChart('miniChart1', {
        type: 'pie',
        labels: data.generos,
        data: data.conteoGenero,
        label: 'Distribución por Género',
        backgroundColor: ['#e74c3c', '#3498db', '#9b59b6'] // Rojo, Azul, Morado
    });
    
    // 3. Gráfica de salarios
    createChart('miniChart2', {
        type: 'bar',
        labels: data.deptosSalario,
        data: data.salariosProm,
        label: 'Salario Promedio',
        backgroundColor: '#2ecc71',
        options: {
            indexAxis: 'y'
        }
    });
    
    // 4. Gráfica de antigüedad
    createChart('miniChart3', {
        type: 'doughnut',
        labels: data.rangosAntiguedad,
        data: data.conteoAntiguedad,
        label: 'Antigüedad de Empleados',
        backgroundColor: ['#3498db', '#2ecc71', '#f1c40f', '#e67e22']
    });
}

// Función para crear gráficas
function createChart(canvasId, {type, labels, data, label, backgroundColor, options = {}}) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return;
    
    // Destruir gráfica existente si hay una
    if (ctx.chart) {
        ctx.chart.destroy();
    }
    
    const defaultOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: label,
                font: {
                    size: 14
                }
            }
        }
    };
    
    ctx.chart = new Chart(ctx, {
        type: type,
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: backgroundColor,
                borderWidth: 1
            }]
        },
        options: {...defaultOptions, ...options}
    });
}

// Configurar eventos del menú
function setupMenuEvents(data) {
    const menuItems = document.querySelectorAll('.menu-lateral a');
    
    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Actualizar clase active
            menuItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');
            
            // Cambiar gráfica principal según selección
            switch(this.dataset.chart) {
                case 'empleados-departamento':
                    updateMainChart('bar', data.departamentos, data.conteoDep, 'Empleados por Departamento', '#3498db');
                    break;
                    
                case 'distribucion-genero':
                    updateMainChart('pie', data.generos, data.conteoGenero, 'Distribución por Género', ['#e74c3c', '#3498db', '#9b59b6']);
                    break;
                    
                case 'salario-departamento':
                    updateMainChart('bar', data.deptosSalario, data.salariosProm, 'Salario Promedio', '#2ecc71', {indexAxis: 'y'});
                    break;
                    
                case 'antiguedad-empleados':
                    updateMainChart('doughnut', data.rangosAntiguedad, data.conteoAntiguedad, 'Antigüedad de Empleados', ['#3498db', '#2ecc71', '#f1c40f', '#e67e22']);
                    break;
            }
        });
    });
}

// Actualizar gráfica principal
function updateMainChart(type, labels, data, label, backgroundColor, options = {}) {
    createChart('mainChart', {
        type: type,
        labels: labels,
        data: data,
        label: label,
        backgroundColor: backgroundColor,
        options: options
    });
}

// Mostrar errores
function showError(message) {
    const errorElement = document.getElementById('chartError');
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
    }
}