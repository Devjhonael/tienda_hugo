from marshmallow_config import ma
from models.product import Product

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Product
        load_instance=True

product_schema=ProductSchema()
products_schema=ProductSchema(many=True)