import json
import sys
from app import create_app
from app.models import *



def cmdArgs():
    from app import db
    arg = sys.argv[1]
    print("Procesando...", end=" ", flush=True)
    with app.app_context():
        if arg == 'create':
            #creamos la base de datos
            
            db.create_all()
            print("\rBase de datos creada", end='', flush=True)
        if arg == "reset":
            db.drop_all()
            db.create_all()
            print("\rBase de datos reseteada", end='', flush=True)
        if arg == "drop":
            db.drop_all()
            print("\rBase de datos borrada", end='', flush=True)
    print('\a')


if __name__ == '__main__':
    app = create_app('config.Config')
    if (len(sys.argv) > 1):
        cmdArgs()
    else:
        app.run(debug=True)
