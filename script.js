const boton = document.getElementById("btn-enviar")
const mensaje = document.getElementById("mensaje-resultado")

// Función para validar email
function validarEmail(email) {
    return email.includes("@") && email.includes(".")
}

// Función para mostrar error
function mostrarError(texto) {
    mensaje.textContent = texto
    mensaje.style.color = "red"
    mensaje.style.fontWeight = "bold"
}

// Función para mostrar éxito
function mostrarExito(texto) {
    mensaje.textContent = texto
    mensaje.style.color = "green"
    mensaje.style.fontWeight = "bold"
}

boton.addEventListener("click", function(event) {
    event.preventDefault()

    const nombre = document.getElementById("campo-nombre").value.trim()
    const email = document.getElementById("campo-email").value.trim()
    const mensajeTexto = document.getElementById("campo-mensaje").value.trim()

    // Validar nombre
    if (nombre === "") {
        mostrarError("Por favor ingresá tu nombre.")
        return
    }

    // Validar email
    if (email === "") {
        mostrarError("Por favor ingresá tu email.")
        return
    }

    if (!validarEmail(email)) {
        mostrarError("El email no tiene un formato válido.")
        return
    }

    // Validar mensaje
    if (mensajeTexto === "") {
        mostrarError("Por favor escribí un mensaje.")
        return
    }

    // Todo OK
    mostrarExito("Gracias " + nombre + "! Tu mensaje fue enviado correctamente.")
})