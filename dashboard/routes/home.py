from flask import Blueprint, render_template

from models import obtener_estadisticas





# ==========================
# BLUEPRINT
# ==========================

home_bp = Blueprint(

    "home",

    __name__

)





# ==========================
# DASHBOARD PRINCIPAL
# ==========================


@home_bp.route("/")

def inicio():


    datos = obtener_estadisticas()



    return render_template(

        "index.html",

        datos=datos

    )