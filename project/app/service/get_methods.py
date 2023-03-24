from datetime import timedelta, date
from app.models import Order, Waiter, Meal, Drink, Association, drink_orders


def get_orders(filters):
    if filters:
        s_from_date = filters.get('orders_date_from', None)
        s_by_date = filters.get('orders_date_by', None)

        if s_from_date and s_by_date:
            from_date = date.fromisoformat(s_from_date)
            by_date = date.fromisoformat(s_by_date)

            by_date += timedelta(days=1)
            from_date -= timedelta(days=1)

            print(from_date, by_date)
            orders = Order.query.filter(Order.orders_date > from_date).filter(by_date > Order.orders_date)
        elif s_from_date:
            from_date = date.fromisoformat(s_from_date)
            from_date -= timedelta(days=1)

            orders = Order.query.filter(Order.orders_date >= from_date)
        elif s_by_date:
            by_date = date.fromisoformat(s_by_date)
            by_date += timedelta(days=1)

            orders = Order.query.filter(by_date >= Order.orders_date)
        else:
            orders = Order.query.all()
    else:
        orders = Order.query.all()

    return list(orders)


def get_waiters(filters):
    if filters:
        sort_by = filters.get('sort-input', False)
        desc = filters.get('desc', False)

        if sort_by == 'first_name':
            if desc:
                waiters = list(Waiter.query.order_by(Waiter.first_name))
                waiters.reverse()
            else:
                waiters = Waiter.query.order_by(Waiter.first_name)
        elif sort_by == 'last_name':
            if desc:
                waiters = list(Waiter.query.order_by(Waiter.last_name))
                waiters.reverse()
            else:
                waiters = Waiter.query.order_by(Waiter.last_name)
        elif sort_by == 'hire_date':
            if desc:
                waiters = list(Waiter.query.all())
                waiters.sort(key=lambda c: c.hire_date, reverse=True)
            else:
                waiters = list(Waiter.query.all())
                waiters.sort(key=lambda c: c.hire_date)
        else:
            waiters = Waiter.query.all()
    else:
        waiters = Waiter.query.all()

    return list(waiters)


def get_bills(order):
    if order:
        drinks = drink_orders.query.filter(drink_orders.order==order)