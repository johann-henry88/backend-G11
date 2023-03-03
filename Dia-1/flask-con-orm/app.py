from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/colegio'
conexion = SQLAlchemy(app=app)


if __name__== '__main__':
    app.run(debug=True)