import os
import sqlite3

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE = os.path.join(
    BASE_DIR,
    "..",
    "database",
    "robuxguardian.db"
)


def conectar():

    conexion = sqlite3.connect(
        DATABASE
    )

    conexion.row_factory = sqlite3.Row

    return conexion


# ==========================
# CREAR TABLAS DASHBOARD
# ==========================


def crear_tablas_dashboard():

    db = conectar()

    cursor = db.cursor()


    # Administradores

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS admins (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            password TEXT,

            role TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP

        )
        """
    )



    db.commit()

    db.close()