from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey, DateTime, Enum, TIMESTAMP, func, extract, case
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
import enum
import json
import unicodedata
import calendar

DB_NAME = 'tarea2'
DB_USERNAME = 'cc5002'
DB_PASSWORD = 'programacionweb'
DB_HOST = 'localhost'
DB_PORT = 3306

DATABASE_URL = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# --- ENUMs ---
class ContactoEnum(enum.Enum):
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"
    X = "X"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    OTRO = "Otro"

class TemaEnum(enum.Enum):
    MUSICA = "música"
    DEPORTE = "deporte"
    CIENCIAS = "ciencias"
    RELIGION = "religión"
    POLITICA = "política"
    TECNOLOGIA = "tecnología"
    JUEGOS = "juegos"
    BAILE = "baile"
    COMIDA = "comida"
    OTRO = "otro"
  
def get_enum_values(enum_class):
    return [member.value for member in enum_class]

# --- Models ---
class Actividad(Base):
    __tablename__ = 'actividad'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100), nullable=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=True)
    dia_hora_inicio = Column(DateTime, nullable=False)
    dia_hora_termino = Column(DateTime, nullable=True)
    descripcion = Column(String(500), nullable=True)

    comuna = relationship("Comuna", back_populates="actividades")
    fotos = relationship("Foto", back_populates="actividad", cascade="all, delete-orphan")
    contactos = relationship("ContactarPor", back_populates="actividad", cascade="all, delete-orphan")
    temas = relationship("ActividadTema", back_populates="actividad", cascade="all, delete-orphan")
    comentarios = relationship("Comentario", back_populates="actividad", cascade="all, delete-orphan")

class Region(Base):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)

    comunas = relationship("Comuna", back_populates="region")

class Comuna(Base):
    __tablename__ = 'comuna'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    region = relationship("Region", back_populates="comunas")
    actividades = relationship("Actividad", back_populates="comuna")

class Foto(Base):
    __tablename__ = 'foto'

    id = Column(Integer, primary_key=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="fotos")

class ContactarPor(Base):
    __tablename__ = 'contactar_por'

    id = Column(Integer, primary_key=True)
    nombre = Column(Enum(ContactoEnum, values_callable=get_enum_values), nullable=False)
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="contactos")

class ActividadTema(Base):
    __tablename__ = 'actividad_tema'

    id = Column(Integer, primary_key=True)
    tema = Column(Enum(TemaEnum, values_callable=get_enum_values), nullable=False)
    glosa_otro = Column(String(15), nullable=True)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="temas")   

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    texto = Column(String(300), nullable=False)
    fecha = Column(TIMESTAMP, nullable=False, default=datetime.now)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="comentarios")


# --- Database Functions ---

def limpiar_texto(texto):
    return texto.lower()

# get from database  

def get_activitie_by_id(act_id):
    session = SessionLocal()
    act = session.query(Actividad).filter_by(id=act_id).first()
    session.close()
    return act

def get_activities(page_size, offset):
    session = SessionLocal()
    activities = session.query(Actividad).limit(page_size).offset(offset).all()
    session.close()
    return activities

def get_last_activities(page_size):
    session = SessionLocal()
    activities = session.query(Actividad).order_by(Actividad.id.desc()).limit(page_size).all()
    session.close()
    return activities

def get_total_activities():
    session = SessionLocal()
    count_act = session.query(func.count(Actividad.id)).scalar()
    session.close()
    return count_act

def get_comuna_by_id(id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=id).first()
    session.close()
    return comuna

def get_region_by_id(id):
    session = SessionLocal()
    region = session.query(Region).filter_by(id=id).first()
    session.close()
    return region

def get_comuna_by_name(name):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(nombre=name).first()
    session.close()
    return comuna

def get_region_by_name(name):
    session = SessionLocal()
    region = session.query(Region).filter_by(nombre=name).first()
    session.close()
    return region

def check_region_comuna(region_name, comuna_name):
    session = SessionLocal()
    region = get_region_by_name(region_name)
    comuna = get_comuna_by_name(comuna_name)
    if(region.id==comuna.region_id):
        session.close()
        return True
    else:
        session.close()
        return False 

def get_fotos(act_id):
    session = SessionLocal()
    fotos = session.query(Foto).filter_by(actividad_id=act_id).all()
    session.close()
    return fotos

def get_tema(act_id):
    session = SessionLocal()
    tema = session.query(ActividadTema).filter_by(actividad_id=act_id).first()
    session.close()
    return tema

def check_valid_tema(tema):
    valid = [e.value.lower() for e in TemaEnum]
    return tema.lower() in valid

def get_contact(act_id):
    session = SessionLocal()
    contactos = session.query(ContactarPor).filter_by(actividad_id=act_id).all()
    session.close()
    return contactos

def check_valid_contact(contact):
    valid = [e.value.lower() for e in ContactoEnum]
    return contact.lower() in valid

def get_comments(act_id):
    session = SessionLocal()
    comments = session.query(Comentario).filter_by(actividad_id=act_id).all()
    session.close()
    return comments

def get_activities_per_day():
    session = SessionLocal()
    results = (
        session.query(func.date(Actividad.dia_hora_inicio).label("dia"), func.count(Actividad.id))
        .group_by(func.date(Actividad.dia_hora_inicio))
        .order_by(func.date(Actividad.dia_hora_inicio))
        .all()
    )
    session.close()
    return [{"date": str(r[0]), "count": r[1]} for r in results]

def get_activities_per_theme():
    session = SessionLocal()
    results = (
        session.query(ActividadTema.tema, func.count(ActividadTema.id))
        .group_by(ActividadTema.tema)
        .order_by(ActividadTema.tema)
        .all()
    )
    session.close()
    return [{"theme": r[0].value, "count": r[1]} for r in results]

def get_activitie_per_time():
    session = SessionLocal()
    horario = case(
        (extract('hour', Actividad.dia_hora_inicio).between(7, 11), 'Mañana'),
        (extract('hour', Actividad.dia_hora_inicio).between(12, 15), 'Mediodia'),
        (extract('hour', Actividad.dia_hora_inicio).between(16, 21), 'Tarde'))

    results = (
        session.query(
            extract('year', Actividad.dia_hora_inicio).label('anio'),
            extract('month', Actividad.dia_hora_inicio).label('mes'),
            horario.label('horario'),
            func.count(Actividad.id).label('cantidad'))
        .group_by('anio', 'mes', 'horario')
        .order_by('anio', 'mes')
        .all()
    )
    session.close()
    
    meses = []
    datos = {}
    for i in results:
        year = int(i.anio)
        month = int(i.mes)
        horario = i.horario
        cantidad = i.cantidad
        label = f"{calendar.month_abbr[month]} {year}"
        if label not in meses:
            meses.append(label)
        if label not in datos:
            datos[label] = {'Mañana': 0, 'Mediodia': 0, 'Tarde': 0}
        if horario in ['Mañana', 'Mediodia', 'Tarde']:
            datos[label][horario] = cantidad

    data_manana = []
    data_mediodia = []
    data_tarde = []

    for i in meses:
        data_manana.append(datos[i]['Mañana'])
        data_mediodia.append(datos[i]['Mediodia'])
        data_tarde.append(datos[i]['Tarde'])

    data = {
        "xAxis": meses,
        "series": [
            {"name": "Mañana", "data": data_manana},
            {"name": "Mediodia", "data": data_mediodia},
            {"name": "Tarde", "data": data_tarde}
        ]
    }
    return data
# fill tables

def create_comment(nombre, texto, act_id):
    session = SessionLocal()
    new_comment = Comentario(nombre=nombre, texto=texto, actividad_id=act_id)
    session.add(new_comment)
    session.commit()
    session.close()

def create_img(ruta, nombre, act_id):
    session = SessionLocal()
    new_img = Foto(ruta_archivo=ruta, nombre_archivo=nombre, actividad_id=act_id)
    session.add(new_img)
    session.commit()
    session.close()

def create_contact(contact, info_contact, act_id):
    session = SessionLocal()
    contact_enum = ContactoEnum(limpiar_texto(contact))
    new_contact = ContactarPor(nombre=contact_enum, identificador=info_contact, actividad_id=act_id)
    session.add(new_contact)
    session.commit()
    session.close()

def create_theme(tema, info_tema, act_id):
    session = SessionLocal()
    tema_enum = TemaEnum(limpiar_texto(tema))
    if not info_tema:
        new_theme = ActividadTema(tema=tema_enum, glosa_otro=None, actividad_id=act_id) 
    else:
        new_theme = ActividadTema(tema=tema_enum, glosa_otro=info_tema, actividad_id=act_id)
    session.add(new_theme)
    session.commit()
    session.close()

def create_activitie(comuna, sector, nombre, email, tel, inicio, fin, descripcion):
    session = SessionLocal()
    comuna_id = get_comuna_by_name(comuna)
    new_act = Actividad(comuna_id=comuna_id.id, sector=sector, nombre=nombre, email=email, celular=tel, 
                        dia_hora_inicio=inicio, dia_hora_termino=fin, descripcion=descripcion)
    session.add(new_act)
    session.commit()
    act_id = new_act.id
    session.close()
    return act_id


