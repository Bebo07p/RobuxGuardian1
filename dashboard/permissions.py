from flask import session


# ==========================
# LOGIN
# ==========================

def logueado():

    return session.get("admin") is True


# ==========================
# ROL ACTUAL
# ==========================

def rol():

    return session.get(
        "admin_role"
    )


# ==========================
# PERMISOS
# ==========================

def tiene_permiso(permisos):

    return rol() in permisos