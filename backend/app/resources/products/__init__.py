from flask_restful import Resource, marshal, reqparse

from app.models.product import Product as ProductModel
from app.schemas import products_schema
from app import db


class Product(Resource):
    def get(self):
        product = ProductModel.query.all()
        return marshal(product, products_schema, 'products')

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True, help='O campo título é obrigatório')
        payload = parser.parse_args()
        
        product = ProductModel()
        product.title = payload.title

        db.session.add(product)
        db.session.commit()

        return marshal(product, products_schema, 'product')
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, help='O campo id é obrigatório')
        parser.add_argument('status', type=bool, required=True, help='O campo status é obrigatório')
        payload = parser.parse_args()

        product = ProductModel.query.get(payload.id)
        product.status = False if payload.status else True
        db.session.add(product)
        db.session.commit()

        return marshal(product, products_schema, 'product')
