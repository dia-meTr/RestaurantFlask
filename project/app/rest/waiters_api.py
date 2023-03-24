from flask_restful import Resource
from flask import abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields

from app import api, db, docs
from app.models import Waiter
from app.rest.constants import WaiterSchema
from app.service import add_to_db, update_waiter, get_waiters


class PostWaiterSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    hire_date = fields.String()
    dismissal_date = fields.String()
    phone_number = fields.String()
    email = fields.String()


class GetWaiter(MethodResource, Resource):
    @marshal_with(WaiterSchema)
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

    @use_kwargs(PostWaiterSchema, location='json')
    @marshal_with(WaiterSchema)
    def put(self, id, **kwargs):
        """
                    Method which can be used to edit specific waiter using his passport

                    Expects: clients passport : str
                    Modifies: nothing
                    Returns: client
                """

        waiter = update_waiter(id, kwargs)

        if not waiter:
            abort(404)

        return waiter


class GetWaiters(MethodResource, Resource):
    @marshal_with(WaiterSchema(many=True))
    def get(self):
        """
            Method which can be used to get all waiters

            Expects: nothing
            Modifies: nothing
            Returns: waiters
        """

        #waiters = get_waiters(kwargs)

        waiters = Waiter.query.all()

        return waiters

    @use_kwargs(PostWaiterSchema)
    @marshal_with(WaiterSchema)
    def post(self, **kwargs):
        """
            Method which can be used to add new waiter to the database

            Expects: nothing
            Modifies: nothing
            Returns: created client
        """
        #args = waiter_put_args.parse_args()
        client = add_to_db(Waiter, **kwargs)

        return client


api.add_resource(GetWaiter, '/json_waiters/<int:id>')
api.add_resource(GetWaiters, '/json_waiters')

docs.register(GetWaiter)
docs.register(GetWaiters)

