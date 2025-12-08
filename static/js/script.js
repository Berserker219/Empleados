

// document.addEventListener('DOMContentLoaded', function() {
//     let currentIndex = 0;
//     const slides = document.querySelectorAll('.carousel-item');
//     const totalSlides = slides.length;

//     function showSlide(index) {
//         const carouselInner = document.querySelector('.carousel-inner');
//         const offset = -index * 100;
//         carouselInner.style.transform = `translateX(${offset}%)`;
//     }

//     function nextSlide() {
//         currentIndex = (currentIndex + 1) % totalSlides;
//         showSlide(currentIndex);
//     }

//     function prevSlide() {
//         currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
//         showSlide(currentIndex);
//     }

//     // Cambiar de slide automáticamente cada 5 segundos
//     setInterval(nextSlide, 5000);

//     // Asignar eventos a los botones de control
//     document.querySelector('.carousel-control.next').addEventListener('click', nextSlide);
//     document.querySelector('.carousel-control.prev').addEventListener('click', prevSlide);
// });

// Solo inicializar slideshow si existe el carrusel
document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.carousel');
    if (!carousel) return;
    
    const slides = document.querySelectorAll('.slide');
    if (slides.length === 0) return;

    let currentSlide = 0;
    let slideInterval;
    
    function showSlide(n) {
        slides.forEach(slide => {
            slide.style.display = 'none';
        });
        currentSlide = (n + slides.length) % slides.length;
        slides[currentSlide].style.display = 'block';
    }
    
    function nextSlide() {
        showSlide(currentSlide + 1);
    }
    
    function prevSlide() {
        showSlide(currentSlide - 1);
    }
    
    // Inicializar
    showSlide(0);
    
    // Configurar intervalo
    slideInterval = setInterval(nextSlide, 3000);
    
    // Botones de control
    const prevBtn = document.querySelector('.carousel-control.prev');
    const nextBtn = document.querySelector('.carousel-control.next');
    
    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            clearInterval(slideInterval);
            prevSlide();
            slideInterval = setInterval(nextSlide, 3000);
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            clearInterval(slideInterval);
            nextSlide();
            slideInterval = setInterval(nextSlide, 3000);
        });
    }
    
    // Pausar al pasar el mouse
    carousel.addEventListener('mouseenter', function() {
        clearInterval(slideInterval);
    });
    
    carousel.addEventListener('mouseleave', function() {
        slideInterval = setInterval(nextSlide, 3000);
    });
    
    // Pausar al tocar en móviles
    carousel.addEventListener('touchstart', function() {
        clearInterval(slideInterval);
    });
    
    carousel.addEventListener('touchend', function() {
        slideInterval = setInterval(nextSlide, 3000);
    });
});