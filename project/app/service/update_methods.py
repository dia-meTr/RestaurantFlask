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


def update_order(id, **kwargs):
    order = Order.query.get(id)
    if order is None:
        return None

    waiter = kwargs.get('waiter_id')
    if waiter:
        order.waiter_id = waiter

    table = kwargs.get('table')
    if table:
        order.table = table

    status = kwargs.get('status_id')
    if status:
        order.status_id = status

    db.session.commit()

    return order


