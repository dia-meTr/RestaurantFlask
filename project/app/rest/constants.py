from datetime import datetime
from flask_restful import fields, reqparse
from app.models.menu import Meals

order_put_args = reqparse.RequestParser()
order_put_args.add_argument('waiter', type=int)
order_put_args.add_argument('table', type=int)
order_put_args.add_argument('status', type=int)
order_put_args.add_argument('orders_date', type=str)

resource_meal_fields = {
        'id': fields.Integer,
        'title': fields.String,
        'description': fields.String,
        'weight': fields.Float,
        'price': fields.Float
}

resource_drink_fields = {
        'title': fields.String,
        'description': fields.String,
        'size': fields.Float,
        'price': fields.Float
}

resource_order_fields = {
    'waiter_name': fields.String,
    'table': fields.Integer,
    'orders_date': fields.String,
    'status_value': fields.String,
    'get_meals': fields.Nested(resource_meal_fields),
    'get_drinks': fields.Nested(resource_drink_fields),
    'total_cost': fields.Float
}

