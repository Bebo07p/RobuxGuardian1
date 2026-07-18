import sqlite3
import os



# ==========================
# RUTA DATABASE
# ==========================

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

DATABASE = os.path.join(

    ROOT_DIR,

    "database",

    "robuxguardian.db"

)



# ==========================
# CONEXION
# ==========================

def conectar():

    return sqlite3.connect(

        DATABASE

    )



# ==========================
# EJECUTAR SQL
# ==========================

def ejecutar(

    query,

    parametros=()

):

    db = conectar()

    cursor = db.cursor()

    cursor.execute(

        query,

        parametros

    )

    db.commit()

    resultado = cursor.fetchall()

    db.close()

    return resultado



# ==========================
# CREAR TABLAS
# ==========================

def crear_tablas():

    db = conectar()

    cursor = db.cursor()



    # ==========================
    # TICKETS
    # ==========================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS tickets (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user TEXT,

        subject TEXT,

        message TEXT,

        status TEXT,

        created_at TEXT,

        claimed_by TEXT,

        claimed_at TEXT,

        closed_by TEXT,

        closed_at TEXT

    )

    """)



    cursor.execute(

        "PRAGMA table_info(tickets)"

    )

    columnas_tickets = [

        columna[1]

        for columna in cursor.fetchall()

    ]



    nuevas_columnas_tickets = [

        "claimed_by TEXT",

        "claimed_at TEXT",

        "closed_by TEXT",

        "closed_at TEXT"

    ]



    for columna in nuevas_columnas_tickets:

        nombre = columna.split()[0]

        if nombre not in columnas_tickets:

            cursor.execute(

                f"ALTER TABLE tickets ADD COLUMN {columna}"

            )


    # ==========================
    # EVIDENCIA TICKETS
    # ==========================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS ticket_messages (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        ticket_id INTEGER,

        ticket_channel TEXT,

        author TEXT,

        author_id TEXT,

        message TEXT,

        attachments TEXT,

        created_at TEXT

    )

    """)



    # ==========================
    # USUARIOS
    # ==========================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        discord_id TEXT,

        username TEXT,

        roblox TEXT,

        created_at TEXT

    )

    """)



    # ==========================
    # ENTREGAS ROBUX
    # ==========================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS deliveries (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        discord_id TEXT,

        discord_username TEXT,

        roblox_id TEXT,

        roblox_username TEXT,

        amount INTEGER,

        reason TEXT,

        delivered_by TEXT,

        created_at TEXT

    )

    """)



    # ==========================
    # REPARAR DELIVERY
    # ==========================

    cursor.execute(

        "PRAGMA table_info(deliveries)"

    )

    columnas_deliveries = [

        columna[1]

        for columna in cursor.fetchall()

    ]



    nuevas_columnas_deliveries = [

        "discord_id TEXT",

        "discord_username TEXT",

        "roblox_id TEXT",

        "roblox_username TEXT",

        "reason TEXT"

    ]



    for columna in nuevas_columnas_deliveries:

        nombre = columna.split()[0]

        if nombre not in columnas_deliveries:

            cursor.execute(

                f"ALTER TABLE deliveries ADD COLUMN {columna}"

            )


    # ==========================
    # LOGS
    # ==========================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS logs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        action TEXT,

        user TEXT,

        created_at TEXT

    )

    """)




    # ==========================
    # CUENTAS ROBLOX
    # ==========================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS roblox_accounts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        discord_id TEXT UNIQUE,

        discord_username TEXT,

        roblox_id TEXT,

        roblox_username TEXT,

        display_name TEXT,

        description TEXT,

        avatar TEXT,

        created TEXT,

        verified INTEGER DEFAULT 1

    )

    """)




    # ==========================
    # REPARAR COLUMNAS ROBLOX
    # ==========================

    cursor.execute(

        "PRAGMA table_info(roblox_accounts)"

    )


    columnas_roblox = [

        columna[1]

        for columna in cursor.fetchall()

    ]



    nuevas_columnas_roblox = [

        "discord_username TEXT",

        "roblox_id TEXT",

        "roblox_username TEXT",

        "display_name TEXT",

        "description TEXT",

        "avatar TEXT",

        "created TEXT",

        "verified INTEGER DEFAULT 1"

    ]



    for columna in nuevas_columnas_roblox:


        nombre = columna.split()[0]


        if nombre not in columnas_roblox:


            cursor.execute(

                f"ALTER TABLE roblox_accounts ADD COLUMN {columna}"

            )





    # ==========================
    # GUARDAR CAMBIOS
    # ==========================



# ==========================
# ANALISIS USUARIOS
# ==========================

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS user_analysis(
                   
                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                   discord_id TEXT UNIQUE,

                   total_tickets INTEGER DEFAULT 0,

                   total_deliveries INTEGER DEFAULT 0,

                   total_robux INTEGER DEFAULT 0,

                   risk INTEGER DEFAULT 0,

                   last_delivery TEXT
                   
                   )
                   """)



    db.commit()

    db.close()



    print(

        "✅ Base de datos preparada"

    )