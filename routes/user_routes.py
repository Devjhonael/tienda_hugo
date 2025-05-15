from controllers.user_controller import UserListResource,UserResource

def register_user_routes(api):  
    api.add_resource(UserListResource, '/users') 
    api.add_resource(UserResource, '/user/<int:id>') 