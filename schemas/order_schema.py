from marshmallow_config import ma
from models.order import Order

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Order
        load_instance=True

order_schema=OrderSchema()
orders_schema=OrderSchema(many=True)