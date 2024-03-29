from app import db
from sqlalchemy.sql import func
from .waiter import Waiter
from .menu import Meal, Drink


class Association(db.Model):
    __tablename__ = 'meal_order'
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), primary_key=True)
    amount = db.Column(db.Integer, server_default='1')

    order = db.relationship("Order", back_populates="meal")
    meal = db.relationship("Meal")

    @property
    def meal_info(self):
        meal = Meal.query.filter(Meal.id == self.meal_id).first()
        return meal

    @property
    def cost(self):
        meal = Meal.query.filter(Meal.id == self.meal_id).first()
        cost = meal.price * self.amount

        return cost


drink_orders = []


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.status}'


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    waiter_id = db.Column(db.Integer, db.ForeignKey('waiters.id'), nullable=False)
    table = db.Column(db.Integer)
    orders_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), server_default='1')

    meal = db.relationship("Association", back_populates="order")

    @property
    def waiter_name(self):
        waiter = Waiter.query.filter(Waiter.id == self.waiter_id).first()
        return f'{waiter.first_name} {waiter.last_name}'

    @property
    def status_value(self):
        stat = Status.query.filter(Status.id == self.status_id).first()
        return f'{stat.status}'

    @property
    def get_meals(self):
        meals = self.meals
        return meals

    @property
    def get_drinks(self):
        drinks = []  # self.drinks
        return drinks

    @property
    def total_cost(self):
        return 0

    def __repr__(self):
        return f'{self.table}, {self.total_cost}'
