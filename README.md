# Template serfver with flask

## create virtualenv

```bash
python -m venv venv
```

```bash
 venv\Scripts\activate
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python run.py
```

## Contenido

- [x] [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [x] [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [x] [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [x] [Flask-Script](https://flask-script.readthedocs.io/en/latest/)


## carpetas


- .env (archivo de configuracion)
- config.py (configuracion de la app)
- requirements.txt (dependencias)
- run.py (ejecucion de la app)
- app (carpeta de la app)
    - static (carpeta de archivos estaticos)
      - css (carpeta de archivos css)
      - fonts (carpeta de archivos de fuentes)
      - img (carpeta de imagenes)
      - js (carpeta de archivos js)
    - templates (carpeta de templates)
      - admin (carpeta de templates de admin)
      - components (carpeta de componentes)
      - comun (carpeta de templates de componentes comunes)
      - email (carpeta de templates de email)
      - json (carpeta de json)
      - layouts (carpeta detemplates de layouts[header, footer, etc])
      - 404.html (template de error 404)
      - index.html (template de index)
    - init.py (inicializacion de la app)
    - models.py (modelo de la base de datos)
    - routes.py (rutas de la app)

  