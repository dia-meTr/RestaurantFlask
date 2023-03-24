from marshmallow import Schema, fields


class OrdersSchema(Schema):
    id = fields.Integer()
    waiter_name = fields.String()
    table = fields.Integer()
    orders_date = fields.String()
    status_value = fields.String()
    total_cost = fields.Float()


class MealSchema(Schema):
    id = fields.Integer(),
    title = fields.String(),
    description = fields.String(),
    weight = fields.Float(),
    price = fields.Float()


class MealBillSchema(Schema):
    meal_id = fields.Integer()
    meal = fields.Nested(MealSchema())
    order_id = fields.Integer()
    amount = fields.Integer()
    cost = fields.Float()


class DrinkSchema(Schema):
    title = fields.String(),
    description = fields.String(),
    size = fields.Float(),
    price = fields.Float()


class DrinkBillSchema(Schema):
    meal_id = fields.Integer()
    meal = fields.Nested(DrinkSchema())
    order_id = fields.Integer()
    amount = fields.Integer()
    cost = fields.Float()


class OrderSchema(Schema):
    id = fields.Integer()
    waiter_name = fields.String()
    table = fields.Integer()
    orders_date = fields.String()
    status_value = fields.String()
    total_cost = fields.Float()
    meals = fields.Nested(MealBillSchema()),
    get_drinks = fields.Nested(DrinkBillSchema()),


class WaiterSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    hire_date = fields.String()
    dismissal_date = fields.String()
    phone_number = fields.String()
    email = fields.String()



from flask_restful import fields, reqparse


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
