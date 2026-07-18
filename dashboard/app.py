import os

from datetime import timedelta

from flask import Flask, redirect, url_for


from routes.home import home_bp
from routes.auth import auth_bp
from routes.tickets import tickets_bp
from routes.admins import admins_bp
from routes.users import users_bp
from routes.deliveries import deliveries_bp
from routes.antifraude import antifraude_bp
from routes.settings import settings_bp
from database import crear_tablas_dashboard





# ==========================
# DIRECTORIO BASE
# ==========================


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)







# ==========================
# FLASK CONFIG
# ==========================


app = Flask(


    __name__,


    template_folder=os.path.join(
        BASE_DIR,
        "templates"
    ),


    static_folder=os.path.join(
        BASE_DIR,
        "static"
    )


)






# ==========================
# SEGURIDAD
# ==========================


app.secret_key = "RobuxGuardian_Enterprise_2026"




# Mantener login activo

app.permanent_session_lifetime = timedelta(
    days=7
)









# ==========================
# REGISTRO DE RUTAS
# ==========================



app.register_blueprint(
    home_bp
)



app.register_blueprint(
    auth_bp
)



app.register_blueprint(
    tickets_bp
)



app.register_blueprint(
    admins_bp
)



app.register_blueprint(
    users_bp
)



app.register_blueprint(
    deliveries_bp
)



app.register_blueprint(
    antifraude_bp
)



app.register_blueprint(
    settings_bp
)










# ==========================
# MANEJO DE ERRORES
# ==========================



@app.errorhandler(404)
def pagina_no_encontrada(error):


    return """
    
    <h1>404</h1>

    <p>Página no encontrada</p>

    """,404







@app.errorhandler(500)
def error_servidor(error):


    return """
    
    <h1>Error interno</h1>

    <p>RobuxGuardian tuvo un problema</p>

    """,500











# ==========================
# INICIAR SERVIDOR
# ==========================



if __name__ == "__main__":


    crear_tablas_dashboard()


    print(
        """
        
🛡️ ===============================
   RobuxGuardian Enterprise
   Dashboard iniciado
===============================

🌐 http://127.0.0.1:5000

        """
    )


print("\n===== RUTAS =====")

for regla in sorted(app.url_map.iter_rules(), key=lambda r: str(r)):
    print(regla)

print("=================\n")


app.run(


        host="0.0.0.0",


        port=5000,


        debug=True


    )