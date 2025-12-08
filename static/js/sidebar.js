// Manejo simple del sidebar
document.addEventListener('DOMContentLoaded', function() {
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const closeBtn = document.getElementById('closeBtn');
    const sidebar = document.getElementById('sidebar');
    
    let isOpen = false;
    
    // Abrir sidebar
    function openSidebar() {
        sidebar.classList.add('active');
        isOpen = true;
        // Prevenir scroll del body cuando sidebar está abierto
        document.body.style.overflow = 'hidden';
    }
    
    // Cerrar sidebar
    function closeSidebar() {
        sidebar.classList.remove('active');
        isOpen = false;
        // Restaurar scroll
        document.body.style.overflow = 'auto';
    }
    
    // Event listeners
    if (hamburgerBtn) {
        hamburgerBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            openSidebar();
        });
    }
    
    if (closeBtn) {
        closeBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            closeSidebar();
        });
    }
    
    // Cerrar sidebar al hacer clic fuera
    document.addEventListener('click', function(e) {
        if (isOpen && !sidebar.contains(e.target) && e.target !== hamburgerBtn) {
            closeSidebar();
        }
    });
    
    // Cerrar sidebar con tecla Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && isOpen) {
            closeSidebar();
        }
    });
});