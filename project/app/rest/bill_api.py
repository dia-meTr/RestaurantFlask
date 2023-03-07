from flask_restful import Resource, marshal_with
from flask import abort, request

from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource

from app import api, db, docs
from app.models import Association, drink_orders
from app.rest.constants import ResourceMealBill
from app.service import add_to_db


class MealBill(MethodResource, Resource):
    @marshal_with(ResourceMealBill)
    def get(self, order_id, meal_id):
        item = Association.query.filter(Association.order_id == order_id, Association.meal_id == meal_id).first()

        if not item:
            abort(404)

        # order.meals.append()

        return item

    def post(self, order_id, meal_id):
        item = Association.query.filter(Association.order_id == order_id, Association.meal_id == meal_id).first()

        if item:
            abort(500)

        add_to_db(Association, order_id=order_id, meal_id=meal_id)

        return item


api.add_resource(MealBill, '/json_meal_item/<int:order_id>/<int:meal_id>')
