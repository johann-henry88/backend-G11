from flask_restful import Resource, request
from db import conexion
from models.categoria_model import Producto
from dtos.producto_dto import ProductoDto, MostrarProductoDto
from os import path
from werkzeug.utils import secure_filename
from uuid import uuid4
class ProductosController(Resource):
    def post(self):
        data = request.form
        # TODO: Validar que tengamos esa llave en el formulario llamada 'imagen
        # TODO: validar que solo sean imagenes
        imagen = request.files.get('imagen')
        # TODO: agregar un uuid al nombre de la imagen y sea un nombre valido
        # TODO: no recibir imagenes que pesen mas de 10MB
        #                  B  >  KB  >  MB
        CONTENIDO_MAXIMO = 10 * 1024 * 1024 
        try:
            if imagen is None:  
                raise Exception("Se necesita una imagen para poder crear el producto")
            
            if  mimetype_valido not in imagen.mimetype:
                raise Exception('El archivo no es un archivo valido')
            
            if imagen.content_length > CONTENIDO_MAXIMO:
                raise Exception('El archivo supera los 10Mb')
            
            dto = ProductoDto()
            nombre_seguro = secure_filename(uuid4().hex + '-' + imagen.filename)
            data_serializada = dto.load(data)
            nuevo_producto = Producto(**data_serializada)

            conexion.session.add(nuevo_producto)
            imagen.save(path.join('imagenes', data['imagen']))

            conexion.session.commit()
            return {
                'message': 'Producto creado exitosamente'
            }
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
            