import os

from datetime import datetime

from db.database import conectar





BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)



EXPORT_HTML = os.path.join(

    BASE_DIR,

    "exports",

    "html"

)



os.makedirs(

    EXPORT_HTML,

    exist_ok=True

)








def generar_evidencia(

    canal,

    cerrado_por

):


    db = conectar()

    cursor = db.cursor()



    cursor.execute(

        """

        SELECT

            author,

            message,

            attachments,

            created_at

        FROM ticket_messages

        WHERE ticket_channel = ?

        ORDER BY id ASC

        """,

        (

            canal,

        )

    )



    mensajes = cursor.fetchall()



    db.close()





    print(

        f"🔎 Mensajes encontrados para {canal}: {len(mensajes)}"

    )







    if len(mensajes) == 0:


        return None







    fecha = datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )







    html = f"""

<!DOCTYPE html>

<html>

<head>


<meta charset="UTF-8">


<title>

RobuxGuardian | Evidencia

</title>



<style>


body {{

background:#0f172a;

color:white;

font-family:Arial;

padding:30px;

}}



.header {{

text-align:center;

}}



.message {{

background:#1e293b;

padding:15px;

margin:15px 0;

border-radius:12px;

}}



.author {{

color:#38bdf8;

font-weight:bold;

}}



.date {{

color:#94a3b8;

font-size:12px;

}}



</style>


</head>



<body>



<div class="header">


<h1>🛡️ RobuxGuardian</h1>

<h2>Evidencia de Ticket</h2>


<p>

Ticket: {canal}

</p>


<p>

Cerrado por: {cerrado_por}

</p>


<p>

Fecha: {fecha}

</p>


</div>




<hr>

"""







    for msg in mensajes:



        autor = msg[0]

        texto = msg[1]

        archivos = msg[2]

        fecha_msg = msg[3]



        html += f"""

<div class="message">


<div class="author">

{autor}

</div>



<p>

{texto}

</p>



<div class="date">

{fecha_msg}

</div>


"""



        if archivos:


            html += f"""

<p>

📎 Archivos:

<br>

{archivos}

</p>

"""



        html += """

</div>

"""






    html += """

</body>

</html>

"""







    ruta = os.path.join(

        EXPORT_HTML,

        f"{canal}.html"

    )





    with open(

        ruta,

        "w",

        encoding="utf-8"

    ) as archivo:


        archivo.write(

            html

        )






    print(

        f"📄 Evidencia creada: {ruta}"

    )



    return ruta