from flask_restful import fields

products_schema = {
    'id': fields.Integer,
    'title': fields.String,
    'status': fields.Boolean
}