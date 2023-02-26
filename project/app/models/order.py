from app import db
from datetime import date
from .waiters import Waiters
from .menu import Meals, Drinks

meal_orders = db.Table('meal_orders',
                       db.Column('order', db.Integer, db.ForeignKey('orders.id')),
                       db.Column('meal', db.Integer, db.ForeignKey('meals.id'))
                       )

drink_orders = db.Table('drink_orders',
                        db.Column('order', db.Integer, db.ForeignKey('orders.id')),
                        db.Column('drink', db.Integer, db.ForeignKey('drinks.id'))
                        )


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10))


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    waiter = db.Column(db.Integer, db.ForeignKey('waiters.id'))
    table = db.Column(db.Integer)
    status = db.Column(db.Integer, db.ForeignKey('status.id'))
    orders_date = db.Column(db.Date, index=True, default=date.today())

    meals = db.relationship('Meals', secondary=meal_orders, backref='orders')
    drinks = db.relationship('Drinks', secondary=drink_orders, backref='orders')

    @property
    def waiter_name(self):
        waiter = Waiters.query.filter(Waiters.id == self.waiter).first()
        return f'{waiter.first_name} {waiter.last_name}'

    @property
    def status_value(self):
        stat = Status.query.filter(Status.id == self.status).first()
        return f'{stat.status}'

    @property
    def get_meals(self):
        meals = self.meals
        print(meals)
        return meals

    @property
    def get_drinks(self):
        drinks = self.drinks
        print(drinks)
        return drinks

    """
    @property
    def tour_day_cost(self):
        return Waiter.query.get(self.id).day_cost

    @property
    def total_cost(self):
        return self.tour_day_cost * self.days

    def __repr__(self):
        return f'{self.id}, {self.client_pass}'
"""
