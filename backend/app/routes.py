from flask_restful import Api

def load(api: Api) -> Api:
    from app.resources.products import Product
    api.add_resource(Product, "/products")

    return api