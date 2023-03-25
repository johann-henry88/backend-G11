from rest_framework import serializers
from .models import Categoria, Producto

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializers
class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

def paginationSerializer(totalItems, page, perPage):
    itemsPerPage = perPage if totalItems >= perPage else totalItems
