# Proyecto - Desarrollo de Aplicaciones Web  

## Índice
- [Descripción](#descripción)
- [Requisitos previos](#requisitos-previos)
- [Configuración inicial](#configuración-inicial)
- [Estructura del Proyecto](#estructura-del-proyecto)


## Descripción
Aplicación web que permite gestionar actividades recreativas que están siendo desarrolladas en algún sector en particular. El sistema permite agregar una nueva actividad a través de un formulario, acceder a un listado de las actividades que están siendo realizadas, generar comentarios sobre dicha actividad e informar sobre distintas estadísticas de las actividades en la aplicación web. 

## Requisitos previos
Asegúrate de tener instalado lo siguiente:

- **Python**
- **Git**

## Configuración inicial

```bash
git clone https://github.com/devrr0/desarrollo_web_rocio_farias.git
cd flask_app
```

2. Crear y activar un entorno virtual para aislar las dependencias del proyecto

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar las dependencias necesarias con el entorno virtual activado.

```bash
pip install -r requirements.txt
```

4.  Ejecutar el Servidor para ver que todo funcione correctamente.

```bash
flask run
```

5. Entrar a la aplicación:
   
   - Aplicación: [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home)


## Estructura del proyecto
```bash
flask_app/                                   # Aplicación web principal
├── __pycache__/                             # Archivos cacheados
├── database/                                # Base de datos
│   ├── __pycache__/                         # Archivos cacheados de la base de datos
│   ├── create_user.sql                      # Creación de usuario de la base de datos
│   ├── db.py                                # Base de datos SQLAlchemy
│   ├── init_db.py                           # Inicialización de la base de datos
│   ├── region-comuna.sql                    # Popular región y comuna en la base de datos
│   ├── tabla-comentario.sql                 # Agregar tabla comuna a la base de datos
│   └── tarea2.sql                           # Creación base de datos del proyecto
├── static/                                  # Archivos estáticos
│    ├──css/                                 # Archivos CSS del proyecto
│    │  └── index.css                        # Archivo CSS para todo el proyecto
│    ├──img/                                 # Imágenes del proyecto
│    │  ├── upload/                          # Imágenes subidas a la base de datos
│    │  ├── calendar_logo.png                # Imágen para el logo de la aplicación
│    │  └── placeholder.png                  # Imágen de relleno para etiqueta oculta
│    └──js/                                  # Scripts (Javascript)
│       ├── agregar-actividad.js             # Script para el formulario              
│       ├── index.js                         # Script para redireccionar en la portada
│       ├── info-act.js                      # Script para expandir imágenes
│       ├── select.js                        # Script para definir los select del formulario
│       └── stats.js                         # Script para redireccionar en las estadísticas 
├── templates/                               # Plantillas HTML
│    └──html/                                # Plantillas específicas de la app
│       ├── agregar-actividad.html           # Página para agregar una actividad
│       ├── index.html                       # Portada
│       ├── info-act.html                    # Página de información de una actividad
│       ├── listado-actividades.html         # Página de listado de actividades agregadas
│       └── stats.html                       # Página de estadísticas
├── utils/                                   # Validaciones de la app
│    ├── __pycache__/                        # Archivos cacheados de la validación
│    └── validations.py                      # Validación del formulario
├── venv/                                    # Entorno virtual de Python
├── .gitignore                               # Archivos ignorados por Git
├── app.py                                   # Configuración de la aplicación
└── requirements.txt                         # Dependencias del proyecto
README.md                                    # Documentación del proyecto
```