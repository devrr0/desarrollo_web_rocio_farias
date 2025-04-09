# Proyecto - Desarrollo de Aplicaciones Web  

## Índice
- [Descripción](#descripción)
- [Consideraciones del proyecto](#consideraciones-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)


## Descripción
Aplicación web que permite gestionar actividades recreativas que están siendo desarrolladas en algún sector en particular. El sistema permite agregar una nueva actividad a través de un formulario, acceder a un listado de las actividades que están siendo realizadas e informar sobre distintas estadísticas de las actividades en la aplicación web. 

## Consideraciones del proyecto
En el archivo agregar-actividad.js, el cual valida el formulario, queda pendiente guardar la información de cada contacto que se agrega. Se implementó en el archivo una función addContact() que impone limitaciones al agregar un nuevo contacto. Además, en esta misma función se agregaron funcionalidades para facilitar al usuario el seguimiento de que contactos se han agregado.

Por otra parte, al agregar una foto en el formulario se optó mantener un único cuadro de input para ir agregando fotos. Al agregar una foto se incluyó un mensaje que indica que la foto se agregó y el nombre del archivo para así facilitar el seguimiento de las fotos agregadas. Queda a futuro agregar un botón al lado de cada mensaje que permita eliminar una foto que se haya agregado.

## Estructura del proyecto
```bash
app/                                    # Aplicación web principal
├──css/                                 # Archivos CSS del proyecto
│  └── index.css                        # Archivo CSS para todo el proyecto
├──html/                                # Plantillas HTML
│  ├── agregar-actividad.html           # Página para agregar una actividad
│  ├── index.html                       # Portada
│  ├── info-act.html                    # Página de información de una actividad
│  ├── listado-actividades.html         # Página de listado de actividades agregadas
│  └── stats.html                       # Página de estadísticas
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
│  ├── peliculas.png                    # Imágen de actividad agregada
│  └── placeholder.png                  # Imágen de relleno para etiqueta oculta
├──js/                                  # Scripts (Javascript)
│  ├── agregar-actividad.js             # Script para el formulario              
│  ├── index.js                         # Script para redireccionar en la portada
│  ├── info-act.js                      # Script para expandir imágenes
│  ├── listado-actividades.js           # Script para redireccionar en el listado
│  ├── select.js                        # Script para definir los select del formulario
│  └── stats.js                         # Script para redireccionar en las estadísticas
└ README.md                             # Documentación del proyecto
```