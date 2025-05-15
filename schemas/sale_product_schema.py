from marshmallow_config import ma
from models.sale_product import SaleProduct

class SaleProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=SaleProduct
        load_instance=True

sale_product_schema=SaleProductSchema()
sale_products_schema=SaleProductSchema(many=True)