from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Mi primera API con Flask 😁"

@app.route("/alumno")
def alumno():
    return {
        'nombre': 'Johann',
        'edad': '35',
        'promedio': 18
    }
lista_alumnos = [
    {
        'nombre': 'Johann',
        'edad': '35',
        'promedio': 18
    },
    {
        'nombre': 'Carlos',
        'edad': '34',
        'promedio': 18
    }
   ]
@app.route("/alumnos", methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'])
def alumnos():
    return lista_alumnos



@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
  for alumno in lista_alumnos:
    if alumno['nombre'] == nombre:
        return alumno
    return {
       'message': 'El alumno no existe'
    }


# debug=True ==> Si realizamos algún cambio podremos verlo en tiempo real (se reiniciara el servidor)
app.run(debug=True)