from .home_routes import register_home_routes
from .user_routes import register_user_routes
from .cart_routes import register_cart_routes
from .category_routes import register_category_routes
from .inventory_routes import register_inventory_routes
from .order_routes import register_order_routes
from .payment_routes import register_payment_routes
from .product_routes import register_product_routes
from .sale_routes import register_sale_routes


def register_all_routes(api):
    register_home_routes(api)
    register_user_routes(api)
    register_cart_routes(api)
    register_category_routes(api)
    register_inventory_routes(api)
    register_order_routes(api)
    register_payment_routes(api)
    register_product_routes(api)
    register_sale_routes(api)