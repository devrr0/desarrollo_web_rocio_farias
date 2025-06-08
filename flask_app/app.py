from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_cors import cross_origin
from utils.validations import validate_form, validate_form_comment
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
import uuid
from datetime import datetime

UPLOAD_FOLDER = 'img/upload'

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cc5002:programacionweb@localhost:3306/tarea2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'img/upload') 

# --- Auth routes ---

@app.route("/home", methods=["GET"])
def recent_activities():
    PAGE_SIZE = 5
    data = []
    for act in db.get_last_activities(page_size=PAGE_SIZE):      
        act_id = act.id

        comuna = db.get_comuna_by_id(act.comuna_id)         
        foto = db.get_fotos(act_id)[0]                         
        tema = db.get_tema(act_id)                          
        path_img = f"{foto.ruta_archivo}/{foto.nombre_archivo}" 

        data.append({
            "inicio" : act.dia_hora_inicio,
            "termino" : act.dia_hora_termino,
            "comuna" : comuna.nombre,
            "sector" : act.sector,
            "tema" : tema.glosa_otro.capitalize()  if tema.glosa_otro else tema.tema.value.capitalize() ,      
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
            "termino" : act.dia_hora_termino,
            "comuna" : comuna.nombre,
            "sector" : act.sector,
            "tema" : tema.glosa_otro.capitalize()  if tema.glosa_otro else tema.tema.value.capitalize(),
            "organizador" :  act.nombre,      
            "img" : url_for('static', filename=path_img),
            "id" : act.id
        })
    total_pages = (total_activities + PAGE_SIZE - 1) // PAGE_SIZE

    return render_template("html/listado-actividades.html", data=data, page=page, total_pages=total_pages)

@app.route("/activitie/<int:activitie_id>", methods=["GET", "POST"])
def info_activitie(activitie_id):
    if request.method == "GET":
        act = db.get_activitie_by_id(activitie_id)

        comuna = db.get_comuna_by_id(act.comuna_id)   
        tema = db.get_tema(act.id)
        data = {
            "id" : activitie_id,
            "comuna" : comuna.nombre,
            "sector" : act.sector,
            "organizador" : act.nombre,
            "inicio" : act.dia_hora_inicio,
            "termino" : act.dia_hora_termino,
            "tema" : tema.glosa_otro.capitalize()  if tema.glosa_otro else tema.tema.value.capitalize(),
        }

        comments = db.get_comments(act.id)
        comentarios = []
        for comm in comments:
            comentarios.append({
                "nombre" : comm.nombre,
                "fecha" : comm.fecha,
                "comentario" : comm.texto
            })

        fotos = db.get_fotos(act.id)
        data_img = [f'{f.ruta_archivo}/{f.nombre_archivo}' for f in fotos] 

        return render_template("html/info-act.html", act=data, fotos=fotos, comment=comentarios)
    elif request.method == "POST":
        data = request.get_json()

        nombre = data['nombre']
        comText = data['comText']
        act_id = data['act_id']

        if validate_form_comment(nombre, comText):
            db.create_comment(nombre, comText, act_id)  
        return jsonify({"status": "ok"})

@app.route("/comment/<int:activitie_id>", methods=["GET"])
def get_comment(activitie_id):    
    all_comments = db.get_comments(activitie_id)
    comments = []
    for comm in all_comments:
        comments.append({
            "nombre": comm.nombre,
            "comentario": comm.texto,
            "fecha": comm.fecha.strftime('%Y-%m-%d %H:%M')  
        })
    return jsonify({"status": "ok", "data": comments})


@app.route("/post-activitie", methods=["GET", "POST"])
def post_activitie():
    if request.method == "POST":
        region = request.form.get('select-region')
        comuna = request.form.get('select-comuna')
        sector = request.form.get('sector')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        tel = request.form.get('tel')
        inicio = datetime.strptime(request.form.get('inicio'), "%Y-%m-%dT%H:%M") 
        termino = datetime.strptime(request.form.get('termino'), "%Y-%m-%dT%H:%M") if request.form.get('termino') else None
        descripcion = request.form.get('descripcion')
        tema = request.form.get('select-tema')
        info_tema = request.form.get('info-tema')   

        contactos = []  
        for i in range(6):
            contact_id = f"select-contact{i}"
            info_id = f"info-contact{i}"
            contact = request.form.get(contact_id)
            info = request.form.get(info_id)
            if not contact:
                continue 
            contactos.append((contact, info))

        fotos = [] 
        for j in range(6):
            file_id = f"file{j}"
            if file_id not in request.files:
                continue
            file = request.files[file_id]
            if file and file.filename != "":
                fotos.append(file)          

        if validate_form(region, comuna, sector, nombre, email, tel, request.form.get('inicio'), request.form.get('termino'), tema, info_tema, contactos, fotos):
            imgs = []
            for f in fotos:
                _filename = hashlib.sha256(
                    secure_filename(f.filename).encode("utf-8")
                    ).hexdigest()
                _extension = filetype.guess(f).extension
                img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"

                f.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                imgs.append((img_filename, UPLOAD_FOLDER))

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

@app.route("/stats", methods=["GET"])
def stats():
    return render_template("html/stats.html")

@app.route("/get-stats-data", methods=["GET"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def get_stats_data():    
    data = db.get_activities_per_day()
    data2 = db.get_activities_per_theme()
    data3 = db.get_activitie_per_time()
    return  jsonify({"per_day": data, "per_theme": data2, "per_time": data3})

if __name__ == "__main__":
    app.run(debug=True)