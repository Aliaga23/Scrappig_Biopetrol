# Scrappig\_Biopetrol

Este proyecto tiene como objetivo realizar un web scraping del sitio web de Biopetrol Bolivia para extraer información relevante y generar un archivo KML que puede ser utilizado en aplicaciones de mapas como Google Earth.

## Descripción

El script principal (`main.py`) se encarga de:

* Acceder al sitio web de Biopetrol Bolivia.
* Extraer datos específicos, como ubicaciones de estaciones de servicio.
* Generar un archivo `biopetrol.kml` con la información geoespacial obtenida.

## Estructura del Proyecto

```
Scrappig_Biopetrol/
├── .gitignore
├── README.md
├── biopetrol.kml
└── main.py
```

* `.gitignore`: Especifica los archivos y directorios que Git debe ignorar.
* `README.md`: Este archivo, contiene la descripción del proyecto.
* `biopetrol.kml`: Archivo generado que contiene los datos extraídos en formato KML.
* `main.py`: Script principal que realiza el scraping y genera el archivo KML.

## Requisitos

* Python 3.x
* Bibliotecas adicionales que pueden ser necesarias:

  * `requests`
  * `beautifulsoup4`
  * `simplekml`

Puedes instalar las bibliotecas necesarias utilizando `pip`:

```bash
pip install requests beautifulsoup4 simplekml
```

## Uso

1. Clona el repositorio:

```bash
git clone https://github.com/Aliaga23/Scrappig_Biopetrol.git
cd Scrappig_Biopetrol
```

2. Ejecuta el script principal:

```bash
python main.py
```

3. El script generará un archivo `biopetrol.kml` en el directorio actual.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios que te gustaría realizar.

