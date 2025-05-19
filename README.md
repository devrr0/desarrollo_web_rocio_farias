# Proyecto - Desarrollo de Aplicaciones Web  

## Índice
- [Descripción](#descripción)
- [Consideraciones del proyecto](#consideraciones-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)


## Descripción
Aplicación web que permite gestionar actividades recreativas que están siendo desarrolladas en algún sector en particular. El sistema permite agregar una nueva actividad a través de un formulario, acceder a un listado de las actividades que están siendo realizadas e informar sobre distintas estadísticas de las actividades en la aplicación web. 

## Consideraciones del proyecto
Para poder obtener la información de contactos y fotos de forma segura desde el formulario fue necesario cambiar el frontend desarrollado en la tarea 1. Ahora se incluyeron inputs para cada uno de los elementos que se busca agregar, en vez de manejarlos a través de variables globales. Esto generó un error al validar el tipo de archivo recibido en las fotos desde el frontend, queda a futuro arreglarlo (de momento no se realiza la validación de tipo de foto).

Para la generación del URL que lleva a la información de una actividad se usó /activitie/activitie_id para acceder a la página. Se puede acceder manualmente a ella pero al momento de acceder desde el listado no se logró pasar el elemento actividad.id de Jinja a la función JavaScript que redirige al URL. Para la siguiente tarea queda implementar una forma de pasar un elemento Jinja a JavaScript.




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
│   └── tarea2.sql                           # Creación base de datos del proyecto
├── static/                                  # Archivos estáticos
│    ├──css/                                 # Archivos CSS del proyecto
│    │  └── index.css                        # Archivo CSS para todo el proyecto
│    ├──img/                                 # Imágenes del proyecto
│    │  ├── actividades_por_dia.png          # Gráfico de cantidad de actividades por día
│    │  ├── actividades_por_mes.png          # Gráfico de cantidad de actividades por hora/mes
│    │  ├── actividades_por_tipo.png         # Gráfico de cantidad de actividades por tipo
│    │  └── placeholder.png                  # Imágen de relleno para etiqueta oculta
│    └──js/                                  # Scripts (Javascript)
│       ├── agregar-actividad.js             # Script para el formulario              
│       ├── index.js                         # Script para redireccionar en la portada
│       ├── info-act.js                      # Script para expandir imágenes
│       ├── listado-actividades.js           # Script para redireccionar en el listado
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