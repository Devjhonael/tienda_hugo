from controllers.inventory_controller import InventoryListResource,InventorytResource

def register_inventory_routes(api):  
    api.add_resource(InventoryListResource, '/inventorys') 
    api.add_resource(InventorytResource, '/inventory/<int:id>') 