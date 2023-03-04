from app import db
from app.models import Waiter, Order


def update_waiter(id, new_values):
    waiter = Waiter.query.get(id)
    if waiter is None:
        return None

    if new_values:
        hire_date = new_values.get('hire_date', None)
        if hire_date:
            waiter.hire_date = hire_date

        email = new_values.get('email', None)
        if email:
            waiter.email = email

        dismissal_date = new_values.get('dismissal_date', None)
        if dismissal_date:
            waiter.dismissal_date = dismissal_date

        phone_number = new_values.get('phone_number', None)
        if phone_number:
            waiter.phone_number = phone_number

        db.session.commit()

    return waiter


def update_order(id, new_data):
    order = Order.query.get(id)
    if order is None:
        return None

    if new_data:
        waiter = new_data.get('waiter', None)
        if waiter:
            order.hire_date = waiter

        table = new_data.get('table', None)
        if table:
            order.table = table

        status = new_data.get('status', None)
        if status:
            order.status = status

        orders_date = new_data.get('orders_date', None)
        if orders_date:
            order.orders_date = orders_date

        db.session.commit()

    return order


