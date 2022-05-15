$(document).ready(function () {
    
    $("#ingresar").click(function (event) { 
        event.preventDefault();

        let userEmail = $("#userEmail").val();
        let userPassword = $("#userPassword").val();

        if (userEmail === "usuario@gmail.com" && userPassword === "usuario") {
            alert("Bienvenido, ingresando a tu perfil...");
            window.location.replace("../../publicar/index.html");
        } else {
            alert("Clave o usuario incorrecto, intenta denuevo")
        }

    });
});