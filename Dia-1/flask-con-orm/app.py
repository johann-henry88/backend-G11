from flask import Flask
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from models.nivel_model import Nivel
from models.maestro_model import Maestro
from models.seccion_model import Seccion


# es el encargado de leer el archivo .env si es que existe y agregar
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
# si quiero crear mi conexion en otro archivo e inicializar la configuracion
conexion.init_app(app)

# ahora realizo la inicializacion de mi clase Migrate
# se le pasa la aplicacion como primer parametro y la conexion (instancia de SQLMigrate)
Migrate(app=app, db=conexion)


if __name__== '__main__':
    app.run(debug=True)