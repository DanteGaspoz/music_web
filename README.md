# Music Explorer

Music Explorer es una aplicación web desarrollada con Flask que permite descubrir bandas y artistas underground a partir de otros artistas conocidos.

El proyecto utiliza datos de Last.fm y MusicBrainz para encontrar artistas similares, filtrarlos por género musical, país de origen y popularidad, y mostrar los resultados en una interfaz web sencilla.

## Características

* Búsqueda de artistas similares.
* Filtrado por género musical.
* Filtrado por país de origen.
* Descubrimiento de bandas underground.
* Interfaz web desarrollada con Flask y Jinja.
* Base de datos SQLite para almacenar búsquedas y futuras funcionalidades.

## Tecnologías utilizadas

### Backend

* Python
* Flask
* Requests
* Python Dotenv

### Frontend

* HTML
* CSS
* Jinja2

### Base de datos

* SQLite

### APIs

* Last.fm API
* MusicBrainz API

## Estructura del proyecto

```text
music_web/
│
├── app.py
├── .env
├── requirements.txt
│
├── database/
│   ├── models.py
│   └── database.db
│
├── services/
│   ├── lastfm.py
│   ├── musicbrainz.py
│   └── filters.py
│
├── routes/
│   └── search.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── results.html
│
└── static/
    └── css/
        └── style.css
```

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/music-explorer.git
cd music-explorer
```

### Crear un entorno virtual

```bash
python -m venv venv
```

### Activar el entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto:

```env
LASTFM_API_KEY=tu_api_key
MUSICBRAINZ_API_KEY=tu_api_key
```

## Ejecutar la aplicación

```bash
python app.py
```

Luego abrir:

```text
http://localhost:5000
```

## Cómo funciona

1. El usuario introduce un artista.
2. Last.fm obtiene artistas similares.
3. Se recopila información de cada artista.
4. MusicBrainz obtiene el país de origen.
5. Los resultados se filtran por:

   * Género.
   * País.
   * Número máximo de oyentes.
6. Se muestran las bandas encontradas.

## Objetivos futuros

* Sistema de usuarios.
* Guardar artistas favoritos.
* Búsqueda por ciudad o provincia.
* Mapa interactivo de bandas.
* Integración con Spotify.
* Recomendaciones personalizadas.
* Estadísticas musicales por país.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
