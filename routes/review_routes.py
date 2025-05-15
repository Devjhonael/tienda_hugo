from controllers.review_controller import ReviewListResource,ReviewResource

def register_review_routes(api):  
    api.add_resource(ReviewListResource, '/reviews') 
    api.add_resource(ReviewResource, '/review/<int:id>') 