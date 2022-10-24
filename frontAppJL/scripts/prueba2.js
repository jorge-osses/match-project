
// Mostrar el Formulario desde el Boton

function mostrarFormulario() { 
    var formulario = document.getElementById('Formulario');
    formulario.style.display = "block";  
}

// Validacion de Usuario

function isValid(e){

    e.preventDefault();
    var pass ="astros";    
    var password = document.getElementById("Password2");
    console.log(password);

    if (password.value.match(pass)) {
        window.location.href="https://aulasvirtuales.bue.edu.ar/";
        return true;
    } else {
        alert('No, Por favor Intente de Nuevo!');
        return false;
    }

}

document.querySelector('form').addEventListener('submit', isValid);

