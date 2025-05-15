from marshmallow_config import ma
from models.cart import Cart

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Cart
        load_instance=True

cart_schema=CartSchema()
carts_schema=CartSchema(many=True)