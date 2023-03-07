from app import db


class Meal(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(255))
    weight = db.Column(db.Float)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.title}'


class Drink(db.Model):
    __tablename__ = 'Drinks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(255))
    size = db.Column(db.Float)
    price = db.Column(db.Float, nullable=False)
