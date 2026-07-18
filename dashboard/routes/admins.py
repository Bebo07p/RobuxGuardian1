from flask import Blueprint, render_template, request, redirect, url_for

from database import conectar





# ==========================
# BLUEPRINT
# ==========================


admins_bp = Blueprint(

    "admins",

    __name__

)







# ==========================
# PANEL ADMINISTRADORES
# ==========================


@admins_bp.route("/admins")

def admins():


    db = conectar()

    cursor = db.cursor()



    cursor.execute(
        """
        SELECT *
        FROM admins
        ORDER BY id DESC
        """
    )


    lista_admins = cursor.fetchall()



    db.close()



    return render_template(

        "admins.html",

        admins=lista_admins

    )









# ==========================
# CREAR ADMIN
# ==========================


@admins_bp.route(
    "/admins/crear",
    methods=["POST"]
)

def crear_admin():


    nombre = request.form.get(
        "name"
    )


    password = request.form.get(
        "password"
    )


    role = request.form.get(
        "role"
    )





    db = conectar()

    cursor = db.cursor()





    cursor.execute(
        """
        INSERT INTO admins
        (
            name,
            password,
            role
        )

        VALUES
        (
            ?,
            ?,
            ?
        )
        """,
        (
            nombre,
            password,
            role
        )
    )



    db.commit()

    db.close()





    return redirect(
        url_for(
            "admins.admins"
        )
    )









# ==========================
# ELIMINAR ADMIN
# ==========================


@admins_bp.route(
    "/admins/eliminar/<int:id>",
    methods=["POST"]
)

def eliminar_admin(id):


    db = conectar()

    cursor = db.cursor()



    cursor.execute(
        """
        DELETE FROM admins
        WHERE id = ?
        """,
        (
            id,
        )
    )



    db.commit()

    db.close()



    return redirect(
        url_for(
            "admins.admins"
        )
    )