from flask import Flask, request, render_template

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
Lista_alumnos = [
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
    if request.method == 'GET':
       return Lista_alumnos
    elif request.method == 'POST':
       # metodos para obtener el body (request, json) o (request.get_json())
       Lista_alumnos.append(request,json)
       return Lista_alumnos



@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
  for alumno in Lista_alumnos:
    if alumno['nombre'] == nombre:
        return alumno
    return {
       'message': 'El alumno no existe'
    }
  
  @app.route("/html")
  def html():
     edad = 10
     #return "<button>Dame click</button>"
     return render_template('index.html' edad=edad)
  
  @app.route("/form-data", methods=['POST'])
  def form_data():
     print(request,form)
     return 'Form data recibido exitosamente'
  
  @app.route("/files", methods=['POST'])
  def files():
     print(request.files['foto'])
     return 'Archivo recibido exitosamente'

# debug=True ==> Si realizamos algún cambio podremos verlo en tiempo real (se reiniciara el servidor)
app.run(debug=True)