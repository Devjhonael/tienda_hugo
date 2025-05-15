from controllers.product_controller import ProductListResource,ProductResource

def register_product_routes(api):  
    api.add_resource(ProductListResource, '/products') 
    api.add_resource(ProductResource, '/product/<int:id>') 