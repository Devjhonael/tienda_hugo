from controllers.cart_controller import CartListResource,CartResource

def register_cart_routes(api):  
    api.add_resource(CartListResource, '/carts') 
    api.add_resource(CartResource, '/cart/<int:id>') 