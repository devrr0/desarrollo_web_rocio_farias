import re
import filetype
from datetime import datetime
from database import db

def validate_region_comuna(region, comuna):
    return db.check_region_comuna(region, comuna)

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
    expr = r'^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    return bool(re.search(expr, value))

def validate_phone(value):
    if not value:
        return False
    if not (len(value) == 12):
        return False
    expr = r'^\+569\d{8}$'
    return bool(re.search(expr, value))

def validate_contact(value):
    if not value:
        return False
    if not (len(value) < 6):
        return False
    for c in value:
        contact = c[0]
        info = c[1]
        valid_contact = db.check_valid_contact(contact)
        valid_info = 4 <= len(info) <= 50
        return valid_contact and valid_info

def validate_init_time(value):
    try:
        now = datetime.now()
        start = datetime.fromisoformat(value)
        return now < start
    except ValueError:
        return False

def validate_end_time(init, end):
    if not end:
        return True
    try:
        return datetime.fromisoformat(init) < datetime.fromisoformat(end)
    except ValueError:
        return False

def validate_tema(tema, info):
    if not tema:
        return False
    valid_tema = db.check_valid_tema(tema)
    if info:
        valid_info = 3 <= len(info) <= 15 
        return valid_tema and valid_info
    return valid_tema

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
    
def validate_nombre(value):
    if not value:
        return False
    return 3 <= len(value) <= 80

def validate_comentario(value):
    if not value:
        return False
    return 5 <= len(value)

# Implementar una función que realice todas las validaciones    
def validate_form(region, comuna, sector, nombre, email, tel, inicio, termino, tema, info_tema, contactos, fotos): 
    valid = (validate_region_comuna(region, comuna) and validate_sector(sector) and validate_organizacion(nombre) 
             and validate_email(email) and validate_phone(tel) and validate_init_time(inicio) and validate_end_time(inicio, termino)
             and validate_tema(tema, info_tema) and validate_contact(contactos) and validate_files(fotos))
    return valid

def validate_form_comment(nombre, texto):
    return validate_nombre(nombre) and validate_comentario(texto)