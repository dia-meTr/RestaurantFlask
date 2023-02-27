from flask_restful import Resource, marshal_with
from flask import abort, request

from app import api, db
from app.models import Waiter
from app.rest.constants import resource_waiter_fields, waiter_put_args
from app.service.get_methods import get_waiters
from app.service.update_methods import update_waiter
from app.service.post_methods import add_to_db


class GetWaiter(Resource):
    @marshal_with(resource_waiter_fields)
    def get(self, id):
        """
            Method which can be used to get specific waiter using his id

            Expects: order id : int
            Modifies: nothing
            Returns: waiter
        """

        waiter = Waiter.query.get(id)
        if not waiter:
            abort(404)

        return waiter

    @marshal_with(resource_waiter_fields)
    def put(self, id):
        """
                    Method which can be used to edit specific client using his passport

                    Expects: clients passport : str
                    Modifies: nothing
                    Returns: client
                """
        data = waiter_put_args.parse_args()
        waiter = update_waiter(id, data)

        if not waiter:
            abort(404)

        return waiter


class GetWaiters(Resource):
    @marshal_with(resource_waiter_fields)
    def get(self):
        """
            Method which can be used to get all waiters

            Expects: nothing
            Modifies: nothing
            Returns: waiters
        """

        waiters = get_waiters(request.args)

        return waiters

    @marshal_with(resource_waiter_fields)
    def post(self):
        """
                    Method which can be used to add new client to the database

                    Expects: nothing
                    Modifies: nothing
                    Returns: created client
                """
        args = waiter_put_args.parse_args()
        client = add_to_db(Waiter, **args)

        return client


api.add_resource(GetWaiter, '/json_waiters/<int:id>')
api.add_resource(GetWaiters, '/json_waiters')
