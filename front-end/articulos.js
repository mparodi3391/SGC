const api = 'http://localhost:8000/api/'

async function traerArticulos() {
    const tabla = document.getElementById("tablaArticulos")
    tabla.innerHTML = ""
    const response = await fetch(api+'articulos').then(response => response.json())
    for (var row of response) {
        const fila = document.createElement('tr')
        for (var val in row){
            const celda = document.createElement('td')
            celda.textContent = row[val]
            fila.append(celda)
        }
        tabla.append(fila)
    }
    document.getElementById('tabla').style.display = 'block';
    document.querySelector('.create-art').style.display = 'none'
    document.querySelector('.search-art').style.display = 'none'
    
}

async function traerUnSoloArt() {
    const tabla = document.getElementById("tablaArticulos")
    tabla.innerHTML = ""
    const numero = document.getElementById('id')
    const response = await fetch(api+'articulos/'+numero.value).then(response => response.json())
    const fila = document.createElement('tr')
    for (var val in response){
        const celda = document.createElement('td')
        celda.textContent = response[val]
        fila.append(celda)
    }
    tabla.append(fila)
    document.getElementById('tabla').style.display = 'block';

}

function showCreateForm() {
    document.getElementById('tabla').style.display = 'none';
    document.querySelector('.create-art').style.display = 'grid'
    document.querySelector('.search-art').style.display = 'none'
    
}

function showSearchForm() {
    document.getElementById('tabla').style.display = 'none';
    document.querySelector('.create-art').style.display = 'none'
    document.querySelector('.search-art').style.display = 'grid'
    
}

window.onload = function() {
    const formularioCreacion = document.querySelector('.create-art')
    const formularioBusqueda = document.querySelector('.search-art')

    formularioCreacion.addEventListener('submit', async ()=>{
        let objeto = {}
        let sku = document.getElementById('sku')
        let descripcion = document.getElementById('descripcion')
        let marca = document.getElementById('marca')
        let categoria = document.getElementById('categoria')
        let price = document.getElementById('price')

        objeto['sku'] = sku.value
        objeto['descripcion'] = descripcion.value
        objeto['marca'] = marca.value
        objeto['categoria'] = categoria.value
        objeto['ult_precio_compra'] = Number(price.value)

        const response = await fetch(api+'articulos/', {
            method: 'POST',
            body: JSON.stringify(objeto),
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
            }
        })
        const mensaje = document.createElement('span')
        mensaje.classList.add("alert")
        mensaje.classList.add("m-3")
        if (response.status == '201'){
            mensaje.textContent = 'El articulos ha sido creado con exito'
            mensaje.classList.add("alert-success")
        } else {
            mensaje.textContent = 'Ha ocurrido un error'
            mensaje.classList.add("alert-danger")
        }
        
        formularioCreacion.append(mensaje)
        
        let nodosFormulario = formularioCreacion.querySelectorAll("input[type=text]")
        nodosFormulario.forEach(function(e){
            e.value = '';
        })
    })

    formularioBusqueda.addEventListener('submit', async ()=>{
        let nodosFormulario = formularioBusqueda.querySelectorAll("input[type=text]")
        nodosFormulario.forEach(element => {
            console.log(element.id)
        })
    })
}