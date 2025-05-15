from marshmallow_config import ma
from models.cart_product import CartProduct


class CartProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=CartProduct
        load_instance=True

cart_product_schema=CartProductSchema()
cart_products_schema=CartProductSchema(many=True)