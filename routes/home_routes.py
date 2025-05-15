from controllers.home_controller import HomeController

def register_home_routes(api):
    api.add_resource(HomeController,'/')