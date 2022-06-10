$(document).ready(function () {

    $("#loginForm").submit(function (event) { 
        event.preventDefault();

        let userEmail = $("#userEmail").val();
        let userPassword = $("#userPassword").val();

        if (userEmail === "usuario@gmail.com" && userPassword === "usuario") {
            alert("Bienvenido, ingresando a tu perfil...");
            window.location.replace("../../usuario/inicio/");
            return
        } 

        if (userEmail === "admin@gmail.com" && userPassword === "admin") {
            alert("Bienvenido administrador, ingresando a tu perfil...");
            window.location.replace("../../administrador/inicio/");
            return
        } 

        alert("Clave o usuario incorrecto, intenta denuevo");

    });
});