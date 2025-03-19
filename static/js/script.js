document.addEventListener('DOMContentLoaded', function() {
    const buscadorEmpleados = document.getElementById('buscador-empleados');
    const buscadorEmpleadosAdmin = document.getElementById('buscador-empleados-admin');

    if (buscadorEmpleados) {
        buscadorEmpleados.addEventListener('input', function() {
            const filtro = this.value.toLowerCase();
            const filas = document.querySelectorAll('#lista-empleados tbody tr');

            filas.forEach(fila => {
                const nombre = fila.querySelector('td:nth-child(2)').textContent.toLowerCase();
                const apellido = fila.querySelector('td:nth-child(3)').textContent.toLowerCase();
                if (nombre.includes(filtro) || apellido.includes(filtro)) {
                    fila.style.display = '';
                } else {
                    fila.style.display = 'none';
                }
            });
        });
    }

    if (buscadorEmpleadosAdmin) {
        buscadorEmpleadosAdmin.addEventListener('input', function() {
            const filtro = this.value.toLowerCase();
            const filas = document.querySelectorAll('#administrar tbody tr');

            filas.forEach(fila => {
                const nombre = fila.querySelector('td:nth-child(2)').textContent.toLowerCase();
                const apellido = fila.querySelector('td:nth-child(3)').textContent.toLowerCase();
                if (nombre.includes(filtro) || apellido.includes(filtro)) {
                    fila.style.display = '';
                } else {
                    fila.style.display = 'none';
                }
            });
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;

    function showSlide(index) {
        const carouselInner = document.querySelector('.carousel-inner');
        const offset = -index * 100;
        carouselInner.style.transform = `translateX(${offset}%)`;
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % totalSlides;
        showSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        showSlide(currentIndex);
    }

    // Cambiar de slide automáticamente cada 5 segundos
    setInterval(nextSlide, 5000);

    // Asignar eventos a los botones de control
    document.querySelector('.carousel-control.next').addEventListener('click', nextSlide);
    document.querySelector('.carousel-control.prev').addEventListener('click', prevSlide);
});

