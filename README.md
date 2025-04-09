# Proyecto - Desarrollo de Aplicaciones Web  

## Índice
- [Descripción](#descripción)
- [Estructura del Proyecto](#estructura-del-proyecto)


## Descripción
Aplicación web que permite gestionar actividades recreativas que están siendo desarrolladas en algún sector en particular. El sistema permite agregar una nueva actividad a través de un formulario, acceder a un listado de las actividades que están siendo realizadas e informar sobre distintas estadísticas de las actividades en la aplicación web. 

## Estructura del proyecto
```bash
app/
├──css/                                 # Archivos CSS del proyecto
│  └── index.css                        # Archivo CSS para todo el proyecto
├──html/                                # Plantillas HTML
│  ├── agregar-actividad.html           # Página para agregar una actividad
│  ├── index.html                       # Portada
│  ├── info-act.html                    # Página de información de una actividad
│  ├── listado-actividades.html         # Página de listado de actividades agregadas
│  └──  stats.html                      # Página de estadísticas
├──img/                                 # Imágenes del proyecto
│  ├── actividades_por_dia.png          # Gráfico de cantidad de actividades por día
│  ├── actividades_por_mes.png          # Gráfico de cantidad de actividades por hora/mes
│  ├── actividades_por_tipo.png         # Gráfico de cantidad de actividades por tipo
│  ├── baile.png                        # Imágen de actividad agregada
│  ├── baile2.png                       # Imágen de actividad agregada
│  ├── baile3.png                       # Imágen de actividad agregada
│  ├── comedia.png                      # Imágen de actividad agregada
│  ├── futbol.png                       # Imágen de actividad agregada
│  ├── musica.png                       # Imágen de actividad agregada
│  └── peliculas.png                    # Imágen de actividad agregada
├──js/                                  # Scripts (Javascript)
│  ├── agregar-actividad.js             # Script para el formulario              
│  ├── index.js                         # Script para redireccionar en la portada
│  ├── info-act.js                      # Script para expandir imágenes
│  ├── listado-actividades.js           # Script para redireccionar en el listado
│  ├── select.js                        # Script para definir los select del formulario
│  └── stats.js                         # Script para redireccionar en las estadísticas
└ README.md                             # Documentación del proyecto
```