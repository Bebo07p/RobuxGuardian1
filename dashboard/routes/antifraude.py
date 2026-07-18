from flask import Blueprint, render_template

from models import obtener_usuarios, obtener_perfil





# ==========================
# BLUEPRINT
# ==========================


antifraude_bp = Blueprint(

    "antifraude",

    __name__

)





# ==========================
# ANALISIS ANTIFRAUDE
# ==========================


@antifraude_bp.route("/antifraude")

def antifraude():


    usuarios = obtener_usuarios()


    sospechosos = []



    for usuario in usuarios:


        try:


            perfil = obtener_perfil(

                usuario["discord_id"]

            )


            entregas = len(

                perfil["entregas"]

            )


            tickets = len(

                perfil["tickets"]

            )



            riesgo = 0



            if entregas >= 10:

                riesgo += 30



            if tickets >= 5:

                riesgo += 20



            if riesgo >= 40:


                sospechosos.append({

                    "usuario": usuario,

                    "riesgo": riesgo

                })



        except Exception as e:


            print(

                "Error analizando usuario:",

                e

            )





    return render_template(

        "antifraude.html",

        sospechosos=sospechosos

    )