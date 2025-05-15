from marshmallow_config import ma
from models.category import Category

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Category
        load_instance=True

category_schema=CategorySchema()
categorys_schema=CategorySchema(many=True)