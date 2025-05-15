from controllers.category_controller import CategoryListResource,CategoryResource

def register_category_routes(api):  
    api.add_resource(CategoryListResource, '/categorys') 
    api.add_resource(CategoryResource, '/category/<int:id>') 