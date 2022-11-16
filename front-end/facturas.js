function agregarLinea() {
    let primeraLinea = document.getElementById('primera-linea')
    let lineaNueva = primeraLinea.cloneNode(true)
    lineaNueva.style.display = null;
    let tablaLineas = document.getElementById('lineas-factura')
    tablaLineas.append(lineaNueva)

}

function cambioDeMoneda(select) {
    let monedaEnTabla = document.querySelectorAll('#lineas-factura > tr > td > select#moneda')
    monedaEnTabla.forEach(e =>{
        e.value = select.value
    })
}

window.onload = function() {
    let plusSign = document.getElementById('plus')

    plusSign.addEventListener('mouseover', (event) => {
        plusSign.classList.add('bi-plus-circle-fill')
        plusSign.classList.remove('bi-plus-circle')
    })

    plusSign.addEventListener('mouseleave', (event) =>{
        plusSign.classList.add('bi-plus-circle')
        plusSign.classList.remove('bi-plus-circle-fill')
    })
}