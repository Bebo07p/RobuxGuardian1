from flask import Blueprint, render_template

from models import obtener_entregas





# ==========================
# BLUEPRINT
# ==========================


deliveries_bp = Blueprint(

    "deliveries",

    __name__

)





# ==========================
# LISTA DE ENTREGAS
# ==========================


@deliveries_bp.route("/entregas")

def entregas():


    datos = obtener_entregas()



    return render_template(

        "entregas.html",

        entregas=datos

    )