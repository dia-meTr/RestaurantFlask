from flask_restful import Resource, marshal_with
from flask import abort

from app import api, db
from app.models import Orders
from app.rest.constants import resource_order_fields #, resource_tour_fields, resource_client_fields, tour_put_args, \
#    order_put_args, client_put_args


class GetJsonOrder(Resource):
    @marshal_with(resource_order_fields)
    def get(self, id):
        """
            Method which can be used to get specific order using his id

            Expects: order id : int
            Modifies: nothing
            Returns: order
        """

        order = Orders.query.get(id)
        if not order:
            abort(404)

        return order


api.add_resource(GetJsonOrder, '/json_orders/<int:id>')
