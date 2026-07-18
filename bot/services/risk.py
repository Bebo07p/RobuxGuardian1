from db.database import conectar





class RiskSystem:


    @staticmethod
    def analizar(discord_id):


        db = conectar()

        cursor = db.cursor()



        # ==========================
        # ENTREGAS ROBUX
        # ==========================


        cursor.execute(

            """

            SELECT 

            COUNT(*),

            COALESCE(SUM(amount),0),

            MAX(created_at)

            FROM deliveries

            WHERE discord_id = ?

            """,

            (

                discord_id,

            )

        )


        entrega = cursor.fetchone()



        cantidad_entregas = entrega[0] or 0

        total_robux = entrega[1] or 0

        ultima_entrega = entrega[2] or "Ninguna"





        # ==========================
        # TICKETS
        # ==========================
        
        
        cursor.execute(
            
            """
            SELECT COUNT(*)
            
            FROM tickets
            
            WHERE user LIKE ?
            
            """,
            
            (
                
                f"%{discord_id}%",
                
            )
                
        )


        tickets = cursor.fetchone()[0] or 0





        db.close()





        # ==========================
        # CALCULAR RIESGO
        # ==========================


        riesgo = 0





        # Muchas entregas

        if cantidad_entregas >= 20:

            riesgo += 40

        elif cantidad_entregas >= 10:

            riesgo += 30

        elif cantidad_entregas >= 5:

            riesgo += 15
        
        elif cantidad_entregas >= 3:

            riesgo += 5





        # Muchos robux

        if total_robux >= 10000:

            riesgo += 40


        elif total_robux >= 5000:

            riesgo += 30

        elif total_robux >= 1000:

            riesgo += 15

        elif total_robux >= 100:

            riesgo += 5





        # Muchos tickets

        if tickets >= 10:

            riesgo += 25

        elif tickets >= 5:

            riesgo += 15

        elif tickets >= 2:

            riesgo += 5





        if riesgo >= 60:


            nivel = "🔴 ALTO"

            texto = "Actividad elevada, requiere revisión manual."



        elif riesgo >= 30:


            nivel = "🟡 MEDIO"

            texto = "Actividad moderada detectada."



        else:


            nivel = "🟢 BAJO"

            texto = "Usuario sin actividad sospechosa."







        return {


            "riesgo": riesgo,

            "nivel": nivel,

            "texto": texto,

            "robux": total_robux,

            "entregas": cantidad_entregas,

            "tickets": tickets,

            "ultima": ultima_entrega

        }