from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.categoria_model import Categorias

class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Categorias