// ==========================
// ROBUXGUARDIAN NOTIFICATIONS
// ==========================



document.addEventListener(
    "DOMContentLoaded",
    () => {


        iniciarNotificaciones();


    }

);







// ==========================
// SISTEMA DE NOTIFICACIONES
// ==========================


function iniciarNotificaciones(){



    console.log(
        "🔔 Sistema de notificaciones activo"
    );



}







// ==========================
// CREAR NOTIFICACION
// ==========================


function mostrarNotificacion(
    titulo,
    mensaje,
    tipo="info"
){



    const contenedor =
    document.getElementById(
        "notifications"
    );



    if(!contenedor)
        return;





    let alerta =
    document.createElement(
        "div"
    );




    alerta.className =
    "notification " + tipo;





    alerta.innerHTML = `

        <strong>

            ${titulo}

        </strong>


        <p>

            ${mensaje}

        </p>

    `;





    contenedor.appendChild(
        alerta
    );






    setTimeout(
        () => {


            alerta.remove();


        },

        5000

    );



}







// ==========================
// EJEMPLO
// ==========================


function pruebaNotificacion(){



    mostrarNotificacion(

        "🛡️ Sistema",

        "RobuxGuardian está funcionando correctamente",

        "success"

    );



}