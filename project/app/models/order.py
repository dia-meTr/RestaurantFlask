from app import db
from datetime import date
from .waiter import Waiter
from .menu import Meals, Drinks

meal_orders = db.Table('meal_orders',
                       db.Column('order', db.Integer, db.ForeignKey('orders.id')),
                       db.Column('meal', db.Integer, db.ForeignKey('meals.id')),
                       db.Column('amount', db.Integer),
                       )

drink_orders = db.Table('drink_orders',
                        db.Column('order', db.Integer, db.ForeignKey('orders.id')),
                        db.Column('drink', db.Integer, db.ForeignKey('drinks.id')),
                        db.Column('amount', db.Integer),
                        )


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10))

    def __repr__(self):
        return f'{self.status}'


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    waiter = db.Column(db.Integer, db.ForeignKey('waiters.id'))
    table = db.Column(db.Integer)
    status = db.Column(db.Integer, db.ForeignKey('status.id'))
    orders_date = db.Column(db.Date, index=True, default=date.today())

    meals = db.relationship('Meals', secondary=meal_orders, backref='orders', cascade='all, delete')
    drinks = db.relationship('Drinks', secondary=drink_orders, backref='orders', cascade='all, delete')

    @property
    def waiter_name(self):
        waiter = Waiter.query.filter(Waiter.id == self.waiter).first()
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

    @property
    def total_cost(self):
        return 0

    def __repr__(self):
        return f'{self.table}, {self.total_cost}'
    """
    @property
    def tour_day_cost(self):
        return Waiter.query.get(self.id).day_cost
"""


