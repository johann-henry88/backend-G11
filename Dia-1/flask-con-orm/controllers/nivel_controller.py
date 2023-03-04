from flask_restful import Resource, request
from sqlalchemy.orm import Query, Session
from base_de_datos import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto

class NivelController(Resource):
    # GET, POST, PUT
    def get(self):
        query: Query = conexion.session.query(Nivel)
        # SELECT * FROM niveles;
        resultado = query.all()


        dto = NivelDto()
        # dump > es un metodo en el cual le paso la/las instancias que quieres convertir a tiipos de datos genericos. Si se le pasa mas de una instancia, osea una lista de instancias, se le tiene que adicionar el parametro many=True para indicar 
        print(resultado[0].numero)
        print(resultado[0].descripcion)
        niveles = []
        for nivel in resultado:
            niveles.append({
                'id': nivel.id,
                'numero': nivel.numero,
                'descripcion': nivel.descripcion
            })
        return {
            'contenido': niveles
        }

    def post(self):
        data = request.json
        
        dto = NivelDto()
        # load > aca ke pasamos un diccionario y lo convertira y validara si toda la informacion es correcta, si no lo es, emitira un error y si la informacion esta bien, entonces devolvera un diccionario con la data correcta

        try:
            data_validada = dto.load(data)
            print(data_validada)

            nuevo_nivel = Nivel(numero=data_validada.get('numero'), descripcion=data_validada.get('descripcion'))
            # con el metodo add indicamos que queremos guardar ese nuevo registro
            conexion.session.add(nuevo_nivel)
            # con el metodo commit queremos guardar de manera permanente esa informacion en la base de datos
            conexion.session.commit()

            return {
                'message': 'Nivel creado exitosamente'
            }, 201
        except Exception as error:
             return {
                  'message': 'Error al crear el nivel'
                  'content': error.args
             }

class UnNivelController(Resource):
    def get(self, id):
        query: Query = conexion.session.query(Nivel)
        nivel_encontrado = query.filter_by(id= id).first()
        # TODO: Implementar si no existe ese nivel, retornar un message diciendo que el nivel no existe
        dto = NivelDto()
        resultado = dto.dumpl(nivel_encontrado)

        return {
            'content': resultado
        }

