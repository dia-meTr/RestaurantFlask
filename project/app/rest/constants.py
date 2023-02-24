from datetime import datetime
from flask_restful import fields, reqparse

order_put_args = reqparse.RequestParser()
order_put_args.add_argument('waiter', type=int)
order_put_args.add_argument('table', type=int)
order_put_args.add_argument('status', type=int)
order_put_args.add_argument('orders_date', type=str)


resource_order_fields = {
    'id': fields.Integer,
    'waiter': fields.Integer,
    'table': fields.Integer,
    'status': fields.Integer,
    'orders_date': fields.String,

    'waiter_name': fields.String,
    'status_value': fields.String,
    'total_cost': fields.Float
}
