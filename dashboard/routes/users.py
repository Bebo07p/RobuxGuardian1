from flask import Blueprint, render_template, session, redirect, url_for

from models import obtener_usuarios, obtener_perfil





# ==========================
# BLUEPRINT
# ==========================

users_bp = Blueprint(

    "users",

    __name__

)





# ==========================
# LISTA DE USUARIOS
# ==========================


@users_bp.route("/usuarios")

def usuarios():


    usuarios = obtener_usuarios()



    return render_template(

        "usuarios.html",

        usuarios=usuarios

    )







# ==========================
# PERFIL USUARIO
# ==========================


@users_bp.route("/perfil/<discord_id>")

def perfil(discord_id):


    datos = obtener_perfil(

        discord_id

    )



    return render_template(

        "perfil.html",

        perfil=datos

    )







# ==========================
# PERFIL ADMINISTRADOR
# ==========================


@users_bp.route("/perfil")

def perfil_admin():


    admin = session.get(
        "admin"
    )



    return render_template(

        "perfil.html",

        perfil={

            "usuario": admin,

            "entregas": [],

            "tickets": []

        }

    )







# ==========================
# REDIRECCION PERFIL /
# ==========================


@users_bp.route("/perfil/")

def perfil_con_barra():


    return redirect(

        url_for(
            "users.perfil_admin"
        )

    )