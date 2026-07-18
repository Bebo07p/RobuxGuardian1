from db.database import conectar
from datetime import datetime



class UserAnalysis:



    @staticmethod
    def actualizar_entrega(
        discord_id,
        cantidad
    ):


        db = conectar()

        cursor = db.cursor()



        cursor.execute(
            """
            SELECT *
            FROM user_analysis
            WHERE discord_id = ?
            """,
            (
                discord_id,
            )
        )


        usuario = cursor.fetchone()



        fecha = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )



        if usuario is None:


            cursor.execute(
                """
                INSERT INTO user_analysis
                (
                discord_id,
                total_deliveries,
                total_robux,
                last_delivery
                )

                VALUES(?,?,?,?)
                """,

                (
                    discord_id,
                    1,
                    cantidad,
                    fecha
                )

            )


        else:


            cursor.execute(
                """
                UPDATE user_analysis

                SET

                total_deliveries =
                total_deliveries + 1,

                total_robux =
                total_robux + ?,

                last_delivery = ?

                WHERE discord_id = ?

                """,

                (
                    cantidad,
                    fecha,
                    discord_id
                )

            )



        db.commit()

        db.close()




    @staticmethod
    def obtener(discord_id):


        db = conectar()

        cursor = db.cursor()


        cursor.execute(
            """
            SELECT *
            FROM user_analysis
            WHERE discord_id=?
            """,

            (
                discord_id,
            )

        )


        data = cursor.fetchone()


        db.close()


        return data