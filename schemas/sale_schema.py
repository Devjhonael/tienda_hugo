from marshmallow_config import ma
from models.sale import Sale

class SaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Sale
        load_instance=True

sale_schema=SaleSchema()
sales_schema=SaleSchema(many=True)