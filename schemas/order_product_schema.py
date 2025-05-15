from marshmallow_config import ma
from models.order_product import OrderProduct

class OrderProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=OrderProduct
        load_instance=True

order_product_schema=OrderProductSchema()
order_products_schema=OrderProductSchema(many=True)