from app import db
from app.models import Order, Meal, Drink, Waiter, Association

'''
def delete_tour(id_):
    tour = Tour.query.get(id_)
    if not tour:
        return None

    orders = Order.query.filter(Order.tour_id == tour.id)
    for order in orders:
        db.session.delete(order)

    db.session.delete(tour)
    db.session.commit()

    return tour


def delete_client(passport):
    client = Client.query.get(passport)
    if not client:
        return None

    orders = Order.query.filter(Order.client_pass == client.passport)
    for order in orders:
        db.session.delete(order)
        db.session.commit()

    db.session.delete(client)
    db.session.commit()

    return client
'''


def delete_order(id_):
    order = Order.query.get(id_)
    if not order:
        return None

    #orders = meal_orders.query.filter(meal_orders.order == order.id_)

    #for _ in orders:
    #    db.session.delete(_)
    #    db.session.commit()

    db.session.delete(order)
    db.session.commit()

    return order

