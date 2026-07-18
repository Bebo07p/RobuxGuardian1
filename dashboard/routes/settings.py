from flask import Blueprint, render_template, request





# ==========================
# BLUEPRINT
# ==========================


settings_bp = Blueprint(

    "settings",

    __name__

)





# ==========================
# CONFIGURACIÓN
# ==========================


@settings_bp.route("/config")

def configuracion():


    config = {

        "nombre": "RobuxGuardian Enterprise",

        "version": "2026",

        "estado": "Activo"

    }



    return render_template(

        "config.html",

        config=config

    )





# ==========================
# GUARDAR CONFIG
# ==========================


@settings_bp.route("/config/guardar", methods=["POST"])

def guardar_config():


    # Aquí después conectamos
    # configuraciones reales
    # a SQLite


    return "✅ Configuración guardada"