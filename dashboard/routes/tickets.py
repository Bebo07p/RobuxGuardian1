from flask import Blueprint, render_template

from models import obtener_tickets





# ==========================
# BLUEPRINT
# ==========================


tickets_bp = Blueprint(

    "tickets",

    __name__

)





# ==========================
# LISTA DE TICKETS
# ==========================


@tickets_bp.route("/tickets")

def tickets():


    datos = obtener_tickets()



    return render_template(

        "tickets.html",

        tickets=datos

    )