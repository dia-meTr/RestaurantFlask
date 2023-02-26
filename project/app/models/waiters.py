from app import db
from datetime import date


class Waiters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    hire_date = db.Column(db.Date, index=True, default=date.today())
    phone_number = db.Column(db.String(15))
    email = db.Column(db.String(40))

