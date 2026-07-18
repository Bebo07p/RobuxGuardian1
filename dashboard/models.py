import sqlite3

from database import conectar





# ==========================
# ESTADISTICAS GENERALES
# ==========================


def obtener_estadisticas():

    db = conectar()

    cursor = db.cursor()


    datos = {}



    # USUARIOS VERIFICADOS

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM roblox_accounts
        WHERE verified = 1
        """
    )

    datos["usuarios"] = cursor.fetchone()[0]





    # TICKETS TOTALES

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tickets
        """
    )

    datos["tickets"] = cursor.fetchone()[0]





    # TICKETS PENDIENTES

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tickets
        WHERE LOWER(TRIM(status))
        IN (
            'pendiente',
            'abierto',
            'open',
            'en revisión'
        )
        """
    )

    datos["pendientes"] = cursor.fetchone()[0]





    # ENTREGAS

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM deliveries
        """
    )

    datos["entregas"] = cursor.fetchone()[0]





    # TOTAL ROBUX ENTREGADOS

    cursor.execute(
        """
        SELECT SUM(amount)
        FROM deliveries
        """
    )


    robux = cursor.fetchone()[0]


    datos["robux"] = robux if robux else 0





    db.close()


    return datos







# ==========================
# USUARIOS
# ==========================


def obtener_usuarios():

    db = conectar()

    cursor = db.cursor()


    cursor.execute(
        """
        SELECT
            id,
            discord_id,
            discord_username,
            roblox_username,
            created_at
        FROM roblox_accounts
        ORDER BY id DESC
        """
    )


    usuarios = cursor.fetchall()


    db.close()


    return usuarios







# ==========================
# PERFIL USUARIO
# ==========================


def obtener_perfil(discord_id):

    db = conectar()

    cursor = db.cursor()


    perfil = {}



    cursor.execute(
        """
        SELECT *
        FROM roblox_accounts
        WHERE discord_id = ?
        """,
        (
            discord_id,
        )
    )


    perfil["usuario"] = cursor.fetchone()





    cursor.execute(
        """
        SELECT *
        FROM deliveries
        WHERE discord_id = ?
        ORDER BY id DESC
        """,
        (
            discord_id,
        )
    )


    perfil["entregas"] = cursor.fetchall()





    cursor.execute(
        """
        SELECT *
        FROM tickets
        WHERE user = ?
        ORDER BY id DESC
        """,
        (
            discord_id,
        )
    )


    perfil["tickets"] = cursor.fetchall()



    db.close()


    return perfil







# ==========================
# ENTREGAS ROBUX
# ==========================


def obtener_entregas():

    db = conectar()

    cursor = db.cursor()



    cursor.execute(
        """
        SELECT *
        FROM deliveries
        ORDER BY id DESC
        """
    )


    entregas = cursor.fetchall()



    db.close()


    return entregas







# ==========================
# TICKETS
# ==========================


def obtener_tickets():

    db = conectar()

    cursor = db.cursor()



    cursor.execute(
        """
        SELECT *
        FROM tickets
        ORDER BY id DESC
        """
    )


    tickets = cursor.fetchall()



    db.close()


    return tickets