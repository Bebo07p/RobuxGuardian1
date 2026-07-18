from flask import Blueprint, render_template, request, redirect, url_for, session

from database import conectar





# ==========================
# BLUEPRINT
# ==========================

auth_bp = Blueprint(

    "auth",

    __name__

)





# ==========================
# LOGIN
# ==========================


@auth_bp.route("/login", methods=["GET", "POST"])

def login():


    error = None



    if request.method == "POST":


        usuario = request.form.get(
            "name"
        )


        password = request.form.get(
            "password"
        )



        db = conectar()

        cursor = db.cursor()



        cursor.execute(
            """
            SELECT *
            FROM admins
            WHERE name = ?
            AND password = ?
            """,
            (
                usuario,
                password
            )
        )



        admin = cursor.fetchone()



        db.close()



        if admin:


            session["admin"] = {


                "id": admin["id"],

                "name": admin["name"],

                "role": admin["role"]

            }



            return redirect(

                url_for(
                    "home.inicio"
                )

            )



        else:


            error = "Usuario o contraseña incorrectos"



    return render_template(

        "login.html",

        error=error

    )







# ==========================
# LOGOUT
# ==========================


@auth_bp.route("/logout")

def logout():


    session.clear()


    return redirect(

        url_for(
            "auth.login"
        )

    )