from flask_restful import Resource
from flask import abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource

from marshmallow import Schema, fields
from app import api, docs
from app.models import Meal, Drink
from app.rest.constants import resource_drink_fields, resource_meal_fields


class GetMeal(Resource):
    @marshal_with(MethodResource, Resource)
    def get(self, id):
        """
            Method which can be used to get specific order using his id

            Expects: order id : int
            Modifies: nothing
            Returns: meal
        """

        meal = Meal.query.get(id)
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

        drink = Drink.query.get(id)
        if not drink:
            abort(404)

        return drink


api.add_resource(GetMeal, '/json_meals/<int:id>')
api.add_resource(GetDrink, '/json_drinks/<int:id>')
