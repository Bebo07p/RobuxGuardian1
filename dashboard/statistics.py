from database import conectar


def obtener_estadisticas():

    db = conectar()

    cursor = db.cursor()

    datos = {}

    cursor.execute(
        "SELECT COUNT(*) FROM tickets"
    )

    datos["tickets"] = cursor.fetchone()[0]



    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tickets
        WHERE status='Pendiente'
        """
    )

    datos["pendientes"] = cursor.fetchone()[0]



    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tickets
        WHERE status='Cerrado'
        """
    )

    datos["cerrados"] = cursor.fetchone()[0]



    cursor.execute(
        "SELECT COUNT(*) FROM discord_users"
    )

    datos["usuarios"] = cursor.fetchone()[0]



    cursor.execute(
        """
        SELECT SUM(amount)
        FROM deliveries
        """
    )

    robux = cursor.fetchone()[0]

    datos["robux"] = robux if robux else 0



    cursor.execute(
        "SELECT COUNT(*) FROM blacklist"
    )

    datos["blacklist"] = cursor.fetchone()[0]



    db.close()

    return datos