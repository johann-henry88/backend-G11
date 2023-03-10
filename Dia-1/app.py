from flask import Flask
from flask_migrate import Migrate
from bd import conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:powermusic@localhost:5432/tareas'
conexion.init_app(app)

Migrate(app = app,db = conexion)

if __name__== '__main__':
    app.run(debug=True)