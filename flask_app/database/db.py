from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import enum
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# --- ENUMs ---
class ContactoEnum(enum.Enum):
    WHATSAPP = "WhatsApp"
    TELEGRAM = "Telegram"
    X = "X"
    INSTAGRAM = "Instagram"
    TIKTOK = "Tiktok"
    OTRO = "Otro"

class TemaEnum(enum.Enum):
    MUSICA = "Musica"
    DEPORTE = "Deporte"
    CIENCIAS = "Ciencias"
    RELIGION = "Religion"
    POLITICA = "Politica"
    TECNOLOGIA = "Tecnologia"
    JUEGOS = "Juegos"
    BAILE = "Baile"
    COMIDA = "Comida"
    OTRO = "Otro"
  

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
    dia_hora_fin = Column(DateTime, nullable=True)
    descripcion = Column(String(500), nullable=True)

    comuna = relationship("Comuna", back_populates="actividades")

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
    nombre = Column(Enum(ContactoEnum), nullable=False)
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="contactos")

class ActividadTema(Base):
    __tablename__ = 'actividad_tema'

    id = Column(Integer, primary_key=True)
    tema = Column(Enum(TemaEnum), nullable=False)
    glosa_otro = Column(String(15), nullable=True)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="temas")    

# --- Database Functions ---

# get from database  

def get_activities(page_size, offset):
    session = SessionLocal()
    activities = session.query(Actividad).limit(page_size).offset(offset).all()
    session.close()
    return activities

def get_total_activities():
    return len(Actividad.__table__.columns)

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

def get_contact(act_id):
    session = SessionLocal()
    contactos = session.query(ContactarPor).filter_by(actividad_id=act_id).all()
    session.close()
    return contactos

# fill tables

def create_img(ruta, nombre, act_id):
    session = SessionLocal()
    new_img = Foto(ruta_archivo=ruta, nombre_archivo=nombre, actividad_id=act_id)
    session.add(new_img)
    session.commit()
    session.close()

def create_contact(contacto, info_contact, act_id):
    session = SessionLocal()
    new_contact = ContactarPor(nombre=info_contact, identificador=contacto, actividad_id=act_id)
    session.add(new_contact)
    session.commit()
    session.close()

def create_theme(tema, info_tema, act_id):
    session = SessionLocal()
    if not info_tema:
        new_theme = ActividadTema(tema=tema, glosa_otro=None, actividad_id=act_id) 
    else:
        new_theme = ActividadTema(tema=tema, glosa_otro=info_tema, actividad_id=act_id)
    session.add(new_theme)
    session.commit()
    session.close()

def create_activitie(comuna, sector, nombre, email, tel, inicio, fin, descripcion):
    session = SessionLocal()
    comuna_id = session.query(Comuna).filter_by(nombre=comuna).first()
    new_act = Actividad(comuna_id=comuna_id, sector=sector, nombre=nombre, email=email, celular=tel, 
                        dia_hora_inicio=inicio, dia_hora_termino=fin, descripcion=descripcion)
    session.add(new_act)
    act_id = new_act.id
    session.commit()
    session.close()
    return act_id


