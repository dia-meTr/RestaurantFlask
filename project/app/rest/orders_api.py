from flask_restful import Resource, marshal_with
from flask import abort, request

from app import api, db
from app.models import Order
from app.rest.constants import resource_order_fields, order_put_args
from app.service import delete_order, get_orders, update_order, add_to_db


class GetOrder(Resource):
    @marshal_with(resource_order_fields)
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

    @marshal_with(resource_order_fields)
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

    @marshal_with(resource_order_fields)
    def put(self, id):
        """
            Method which can be used to edit specific order using its id

            Expects: id : int
            Modifies: edit order with specified id
            Returns: order
        """
        data = order_put_args.parse_args()
        order = update_order(id, data)

        if not order:
            abort(404)

        return order


class GetOrders(Resource):
    @marshal_with(resource_order_fields)
    def get(self):
        """
            Method which can be used to get all orders

            Expects: nothing
            Modifies: nothing
            Returns: orders
        """

        waiters = get_orders(request.args)

        return waiters

    @marshal_with(resource_order_fields)
    def post(self):
        """
            Method which can be used to add new orders to the database

            Expects: nothing
            Modifies: nothing
            Returns: created order
        """
        args = order_put_args.parse_args()
        order = add_to_db(Order, **args)

        return order


api.add_resource(GetOrder, '/json_orders/<int:id>')
api.add_resource(GetOrders, '/json_orders')
