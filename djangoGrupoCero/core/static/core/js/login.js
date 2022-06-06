$(document).ready(function () {

    $("#loginForm").validationEngine();
    
    $("#loginForm").submit(function (event) { 
        event.preventDefault();

        let userEmail = $("#userEmail").val();
        let userPassword = $("#userPassword").val();

        if (userEmail === "usuario@gmail.com" && userPassword === "usuario") {
            alert("Bienvenido, ingresando a tu perfil...");
            window.location.replace("../../usuario/inicio/index.html");
            return
        } 

        if (userEmail === "admin@gmail.com" && userPassword === "admin") {
            alert("Bienvenido administrador, ingresando a tu perfil...");
            window.location.replace("../../aceptarRechazarProducto/index.html");
            return
        } 

        alert("Clave o usuario incorrecto, intenta denuevo");
        

    });
});