from marshmallow_config import ma
from models.inventory import Inventory

class InventorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Inventory
        load_instance=True

inventory_schema=InventorySchema()
inventorys_schema=InventorySchema(many=True)