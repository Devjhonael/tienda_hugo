from controllers.sale_controller import SaleListResource,SaleResource

def register_sale_routes(api):  
    api.add_resource(SaleListResource, '/sales') 
    api.add_resource(SaleResource, '/sale/<int:id>') 