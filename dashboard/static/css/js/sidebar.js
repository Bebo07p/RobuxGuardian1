// ==========================
// ROBUXGUARDIAN SIDEBAR JS
// ==========================



document.addEventListener(
    "DOMContentLoaded",
    () => {


        activarMenu();


    }

);






// ==========================
// MENU ACTIVO
// ==========================


function activarMenu(){



    let rutaActual =
    window.location.pathname;




    const enlaces =
    document.querySelectorAll(
        ".sidebar nav a"
    );





    enlaces.forEach(
        enlace => {



            let destino =
            enlace.getAttribute(
                "href"
            );



            if(
                destino === rutaActual
            ){


                enlace.classList.add(
                    "active"
                );


            }





            enlace.addEventListener(
                "click",
                () => {



                    enlaces.forEach(
                        item => {

                            item.classList.remove(
                                "active"
                            );

                        }
                    );



                    enlace.classList.add(
                        "active"
                    );



                }

            );



        }

    );



}