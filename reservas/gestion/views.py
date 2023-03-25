from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Categoria, Producto
from .serializers import PruebaSerializer, CategoriaSerializer, ProductoSerializer

class PruebaView(APIView):
    def get(self, request):
        data = [ {
            'nombre': 'diversion',
            'id': 1
        },{
            'nombre': 'entretenimiento',
            'id': 2
        }]

        return Response(data= data)
    
    def post(self, request: Request):
        # https://www.django-rest-framework.org/api-guide/requests/
        print(request.data)
        data= request.data
        data_serializada = PruebaSerializer(data = data)
        # retornara Verdadero o Falso si la data es correcta
        resultado = data_serializada.is_valid()
        if resultado is True:

            return Response(data= {
                'message': 'Se recibio la prueba'
            })
        else:
            return Response(data= {
                'message': 'La data es invalida',
                # errors > me mostrara los errores que generaron que la data sea incorrecta al momento de serializar 
                'content': data_serializada.errors
            })
    
class CategoriaView(APIView):
    def post(self, request: Request):
        data = request.data
        data_serializada = CategoriaSerializer(data=data)

        resultado = data_serializada.is_valid()
        if resultado:
            print(data_serializada.validated_data)
            nueva_categoria = Categoria(**data_serializada.validated_data)
        # save() > guardar la nueva informacion en la base de datos de manera permanente
            nueva_categoria.save()

            return Response(data={
                'message': 'Categoria creada exitosamente'
            })
        else:
            return Response(data={
                'message': 'Error al crear categoria',
                'content': data_serializada.errors
            })
        
    def get(self, request:Request):
        # https://docs.djangoproject.com/en/4.1/topics/db/queries/
        # SELECT * FROM categorias;
        categorias = Categoria.objects.all()
        # NOTA: cuando se pasa instancias se utiliza el parametro 'instances' y cuando se pasa informacion para validar se utiliza el parametro 'data'
        data_serializada = CategoriaSerializer(instance=categorias, many=True)
        print(categorias[0].nombre)

        return Response(data={
            # convierte las instancias de la clase en diccionario
            'content': data_serializada.data
        })
class UnaCategoriaView(APIView):
    def get(self, request:Request, id):
        print(id)
        categoria_encontrada = Categoria.objects.filter(id = id).first()
        if not categoria_encontrada:
            return Response(data={
                'message': 'Categoria no existe'
            }, status=404)
        resultado = CategoriaSerializer(instance=categoria_encontrada)
        return Response(data= {
            'content': resultado.data
        })
    
    def put(self, request:Request, id):
        categoria_encontrada = Categoria.objects.filter(id = id).first()
        if not categoria_encontrada:
            return Response(data={
                'message': 'Categoria no existe'
            }, status=404)
        
        data = request.data
        data_serializada = CategoriaSerializer(data=data)

        if data_serializada.is_valid():
            categoria_encontrada.nombre = data_serializada.validated_data.get('nombre')
            categoria_encontrada.habilitado = data_serializada.validated_data.get('habilitado')

            # donde sobreescribimos los cambios en la base de datos
            categoria_encontrada.save()

            return Response(data={
                'message': 'Categoria actualizada'
            })
        else:
            return Response(data={
                'message': 'Error al actualizar la categoria',
                'content': data_serializada.errors
            })
        
    def delete(self, request: Request, id):
        categoria_encontrada = Categoria.objects.filter(id = id).first()
        if not categoria_encontrada:
            return Response(data={
                'message': 'Categoria no existe'
            }, status=404)
        
        # DELETE FROM categorias WHERE id = ....;
        # me retorna el total de registros eliminados en una tupla de la siguiente manera
        # (correlativo, {'model': cantidad_elementos_eliminados})
        resultado = Categoria.objects.filter(id = id).delete()
        print(resultado)

        return Response(data={
            'message': 'Categoria eliminada exitosamente'
        })
    
class ProductosView(APIView):
    def post(self, request: Request):
        data = request.data
        data_serializada = ProductoSerializer(data=data)
        if data_serializada.is_valid():
            nuevo_producto = data_serializada.save()
            
            resultado = ProductoSerializer(instance=nuevo_producto)

            return Response(data={
                'message': 'Producto creado exitosamente',
                'content': resultado.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear el producto',
                'content': data_serializada.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request: Request):
        # Pasos para hacer la paginacion manual
        #Primero obtenemos los query params que me serviran para orientarme en la pagina
        page = int(request.query_params.get('page'))
        perPage = int(request.query_params.get('perPage', 10))
        # cuantos te vas a saltar
        skip = (page - 1) * perPage

        #cuantos vas a tomar, es el mismo valor que perPage
        take = perPage * page
        print(skip)
        print(take)
        
        productos = Producto.objects.all()[skip:take]
        data_serializada = ProductoSerializer(instance=productos, many=True)

        return Response(data={
            'content': data_serializada.data
        },status=status.HTTP_200_OK)