from controllers.payment_controller import PaymentListResource,PaymentResource

def register_payment_routes(api):  
    api.add_resource(PaymentListResource, '/payments') 
    api.add_resource(PaymentResource, '/payment/<int:id>') 