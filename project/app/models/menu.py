from app import db


class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(255))
    weight = db.Column(db.Float)
    price = db.Column(db.Float)


class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    title = db.Column(db.String(30))
    size = db.Column(db.Float)
    price = db.Column(db.Float)
