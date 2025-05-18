from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import validate_form
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
import uuid

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cc5002:programacionweb@localhost:3306/tarea2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'img') 

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


# --- Auth routes ---

@app.route("/home", methods=["GET"])
def recent_activities():
    PAGE_SIZE = 5
    data = []
    activities = db.get_activities(page_size=PAGE_SIZE, offset=0)
    for act in activities:      
        act_id = act.id

        comuna = db.get_comuna_by_id(act.comuna_id)         
        foto = db.get_fotos(act_id)[0]                         
        tema = db.get_tema(act_id)                          
        path_img = f"{foto.ruta_archivo}/{foto.nombre_archivo}" 

        data.append({
            "inicio" : act.dia_hora_inicio,
            "termino" : act.dia_hora_fin,
            "comuna" : comuna.nombre,
            "sector" : act.sector,
            "tema" : tema.glosa_otro if tema.glosa_otro else tema.tema,      
            "img" : url_for('static', filename=path_img)
        })    

    return render_template("html/index.html", data=data)

@app.route("/list-activities", methods=["GET"])
def all_activities():
    PAGE_SIZE = 5
    page = request.args.get("page", 1, type=int)
    offset = (page - 1) * PAGE_SIZE

    total_activities = db.get_total_activities()    
    activities = db.get_activities(page_size=PAGE_SIZE, offset=offset)            
    data = []
    for act in activities:
        act_id = act.id

        comuna = db.get_comuna_by_id(act.comuna_id)         
        foto = db.get_fotos(act_id)[0]                         
        tema = db.get_tema(act_id)                          
        path_img = f"{foto.ruta_archivo}/{foto.nombre_archivo}" 

        data.append({
            "inicio" : act.dia_hora_inicio,
            "termino" : act.dia_hora_fin,
            "comuna" : comuna.nombre,
            "sector" : act.sector,
            "tema" : tema.glosa_otro if tema.glosa_otro else tema.tema,
            "organizador" :  act.nombre,      
            "img" : url_for('static', filename=path_img)
        })
    total_pages = (total_activities + PAGE_SIZE - 1) // PAGE_SIZE

    return render_template("html/listado-actividades.html", data=data, page=page, total_pages=total_pages)

@app.route("/activitie/<int:activitie_id>", methods=["GET"])
def info_activitie(activitie_id):
    act = db.get_activitie_by_id(activitie_id)

    comuna = db.get_comuna_by_id(act.comuna_id)
    region = db.get_region_by_id(comuna.region_id)      
    tema = db.get_tema(act.id)
    contactos = db.get_contact(act.id)            
    contacto_str = ', '.join([f"{c.identificador} ({c.nombre})" for c in contactos])

    data = {
        "region" : region.nombre,
        "comuna" : comuna.nombre,
        "sector" : act.sector,
        "organizador" : act.nombre,
        "contacto" : contacto_str,
        "inicio" : act.dia_hora_inicio,
        "termino" : act.dia_hora_fin,
        "tema" : tema.glosa_otro if tema.glosa_otro else tema.tema,
        "descripcion" : act.descripcion
    }

    fotos = db.get_fotos(act.id)
    data_img = [{url_for('static', filename=f"{f.ruta_archivo}/{f.nombre_archivo}" )} for f in fotos]

    return render_template("html/info-act.html", act=data, fotos=data_img)

@app.route("/post-activitie", methods=["GET", "POST"])
def post_activitie():
    if request.method == "POST":
        region = request.form.get('select-region')
        comuna = request.form.get('select-comuna')
        sector = request.form.get('sector')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        tel = request.form.get('tel')
        inicio = request.form.get('inicio')
        termino = request.form.get('termino')
        descripcion = request.form.get('descripcion')
        tema = request.form.get('select-tema')
        info_tema = request.form.get('info-tema')   # si es que se selecciono otro

        contactos = []  
        i = 1
        while True:
            contact_id = f"select-contact{i}"
            info_id = f"info-contact{i}"
            contact = request.form.get(contact_id)
            info = request.form.get(info_id)

            if not contact and not info:
                break 
            contactos.append((contact, info))
            i += 1

        fotos = [] 
        j = 1
        while True:
            file_id = f"file{j}"
            if file_id not in request.files:
                break
            file = request.files[file_id]
            if file and file.filename != "":
                fotos.append(file)
                j += 1     

        if validate_form(region, comuna, sector, nombre, email, tel, inicio, termino, tema, info_tema, contactos, fotos):
            imgs = []
            for f in fotos:
                # 1. generate random name for img
                _filename = hashlib.sha256(
                    secure_filename(f.filename).encode("utf-8")
                    ).hexdigest()
                _extension = filetype.guess(f).extension
                img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"

                # 2. save img as a file
                f.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                imgs.append((img_filename,'img'))

            # 3. save in db
            # agregar actividad
            act_id = db.create_activitie(comuna, sector, nombre, email, tel, inicio, termino, descripcion)
            # agregar imagenes
            for i in imgs:
                db.create_img(i[1], i[0], act_id)
            # agregar tema
            db.create_theme(tema, info_tema, act_id)
            # agregar contacto
            for c in contactos:
                db.create_contact(c[0], c[1], act_id)

        return redirect(url_for("recent_activities"))  
    
    elif request.method == "GET":
        return render_template("html/agregar-actividad.html")



if __name__ == "__main__":
    app.run(debug=True)