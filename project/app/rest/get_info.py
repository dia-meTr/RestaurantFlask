from flask_restful import Resource, marshal_with
from flask import abort

from app import api, db
from app.models import Order, Meals, Drinks, Waiter
from app.rest.constants import resource_order_fields, resource_drink_fields, resource_meal_fields
from app.service.delete_methods import delete_order


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
            Modifies: order with specified id
            Returns: deleted order
        """

        order = delete_order(id)
        if not order:
            abort(404)

        return order


class GetMeal(Resource):
    @marshal_with(resource_meal_fields)
    def get(self, id):
        """
            Method which can be used to get specific order using his id

            Expects: order id : int
            Modifies: nothing
            Returns: meal
        """

        meal = Meals.query.get(id)
        if not meal:
            abort(404)

        return meal


class GetDrink(Resource):
    @marshal_with(resource_drink_fields)
    def get(self, id):
        """
            Method which can be used to get specific order using his id

            Expects: order id : int
            Modifies: nothing
            Returns: order
        """

        drink = Drinks.query.get(id)
        if not drink:
            abort(404)

        return drink


api.add_resource(GetOrder, '/json_orders/<int:id>')
api.add_resource(GetMeal, '/json_meals/<int:id>')
api.add_resource(GetDrink, '/json_drinks/<int:id>')
