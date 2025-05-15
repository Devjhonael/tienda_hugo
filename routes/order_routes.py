from controllers.order_controller import OrderListResource,OrderResource

def register_order_routes(api):  
    api.add_resource(OrderListResource, '/orders') 
    api.add_resource(OrderResource, '/order/<int:id>') 