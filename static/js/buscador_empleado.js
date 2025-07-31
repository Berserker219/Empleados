// document.addEventListener('DOMContentLoaded', function() {
//   const buscadores = [
//     { inputId: 'buscador-empleados', tableId: 'lista-empleados' },
//     { inputId: 'buscador-empleados-admin', tableId: 'administrar' }
//   ];

//   buscadores.forEach(({ inputId, tableId }) => {
//     const input = document.getElementById(inputId);
//     if (input) {
//       input.addEventListener('input', function() {
//         const filtro = this.value.toLowerCase();
//         const filas = document.querySelectorAll(`#${tableId} tbody tr`);
//         filas.forEach(fila => {
//           const nombre = fila.querySelector('td:nth-child(2)').textContent.toLowerCase();
//           const apellido = fila.querySelector('td:nth-child(3)').textContent.toLowerCase();
//           fila.style.display = (nombre.includes(filtro) || apellido.includes(filtro)) ? '' : 'none';
//         });
//       });
//     }
//   });
// });


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