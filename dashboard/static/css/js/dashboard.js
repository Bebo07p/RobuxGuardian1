// ==========================
// ROBUXGUARDIAN DASHBOARD JS
// ==========================



document.addEventListener(
    "DOMContentLoaded",
    () => {



        console.log(
            "🛡️ RobuxGuardian Dashboard cargado"
        );



        iniciarAnimaciones();



        iniciarReloj();



    }

);








// ==========================
// ANIMACIONES DE ENTRADA
// ==========================


function iniciarAnimaciones(){



    const elementos = document.querySelectorAll(
        ".card, .panel-box, .table-container"
    );



    elementos.forEach(
        (elemento, index) => {



            elemento.style.opacity = "0";



            setTimeout(
                () => {


                    elemento.style.opacity = "1";


                    elemento.style.transform =
                    "translateY(0)";


                },

                index * 100

            );



        }

    );



}








// ==========================
// RELOJ DEL SISTEMA
// ==========================


function iniciarReloj(){



    const reloj =
    document.getElementById(
        "system-clock"
    );



    if(!reloj)
        return;





    setInterval(
        () => {



            let fecha =
            new Date();



            reloj.innerHTML =
            fecha.toLocaleString();



        },

        1000

    );



}