import re
import filetype
from datetime import datetime


# verificar la base de datos ??
def validate_region(value):
    return True 

def validate_comuna(value):
    return True

def validate_sector(value):
    return len(value) <= 100

def validate_organizacion(value):
    if not value:
        return False
    return 3 <= len(value) <= 200

def validate_email(value):
    if not value:
        return False
    if not (10 < len(value) <= 100):
        return False
    re = r'^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    return re.test(value)

def validate_phone(value):
    if not value:
        return False
    if not (len(value) == 12):
        return False
    re = r'^\+569\d{8}$'
    return re.test(value)

# validar aqui que sean menos de 5 contactos ??
# le paso una lista con los contactos ??
def validate_contact(value):
    return 4 <= len(value) <= 50

def validate_init_time(value):
    try:
        now = datetime.now()
        start = datetime.fromisoformat(value)
        return now < start
    except ValueError:
        return False

def validate_end_time(init, end):
    try:
        return datetime.fromisoformat(init) < datetime.fromisoformat(end)
    except ValueError:
        return False

def validate_tema(tema, info):
    if not tema:
        return False
    if tema == "Otro":
        return 3 <= len(info) <= 15
    return True

def validate_files(files):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    if not files or not (1 <= len(files) <= 5):
        return False

    for file in files:
        if file.filename == "":
            return False

        ftype_guess = filetype.guess(file)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False
    
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False
        return True

# Implementar una función que realice todas las validaciones    
def validate_form(data): 
    return