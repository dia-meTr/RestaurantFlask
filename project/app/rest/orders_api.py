from flask_restful import Resource
from flask import abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource

from marshmallow import Schema, fields
from app import api, docs, db
from app.models import Order
from app.rest.constants import OrderSchema, OrdersSchema
from app.service import delete_order, get_orders, update_order, add_to_db


class PostOrderSchema(Schema):
    waiter_id = fields.Integer()
    status_id = fields.Integer()
    table = fields.Integer()


class GetOrder(MethodResource, Resource):
    @marshal_with(OrdersSchema)
    def get(self, id):
        """
            Method which can be used to get specific order using his id

            Expects: order id : int
            Modifies: nothing
            Returns: order
        """

        order = Order.query.get(id)
        if not order:
            abort(404)

        return order

    @marshal_with(OrdersSchema)
    def delete(self, id):
        """
            Method which can be used to delete specific order using his id

            Expects: order id : int
            Modifies: deletes order with specified id
            Returns: deleted order
        """

        order = delete_order(id)
        if not order:
            abort(404)

        return order

    @use_kwargs(PostOrderSchema, location='json')
    @marshal_with(OrdersSchema)
    def put(self, id, **kwargs):
        """
            Method which can be used to edit specific order using its id

            Expects: id : int
            Modifies: edit order with specified id
            Returns: order
        """
        # data = order_put_args.parse_args()
        order = update_order(id, **kwargs)

        if not order:
            abort(404)

        return order


class GetOrders(MethodResource, Resource):
    @marshal_with(OrderSchema(many=True))
    def get(self):
        """
            Method which can be used to get all orders

            Expects: nothing
            Modifies: nothing
            Returns: orders
        """

        orders = get_orders(request.args)

        return orders

    @use_kwargs(PostOrderSchema, location='json')
    @marshal_with(OrdersSchema)
    def post(self, **kwargs):
        """
            Method which can be used to add new orders to the database

            Expects: nothing
            Modifies: nothing
            Returns: created order
        """
        # args = order_put_args.parse_args()
        order = add_to_db(Order, **kwargs)

        return order


api.add_resource(GetOrder, '/json_orders/<int:id>')
api.add_resource(GetOrders, '/json_orders')

docs.register(GetOrder)
docs.register(GetOrders)
