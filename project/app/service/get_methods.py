from datetime import timedelta, date

from app.models import Order, Waiter


def get_orders(filters):
    if filters:
        s_from_date = filters.get('tour_date_from', None)
        s_by_date = filters.get('tour_date_by', None)

        if s_from_date and s_by_date:
            from_date = date.fromisoformat(s_from_date)
            by_date = date.fromisoformat(s_by_date)

            by_date += timedelta(days=1)
            from_date -= timedelta(days=1)

            print(from_date, by_date)
            orders = Order.query.filter(Order.tour_date > from_date).filter(by_date > Order.tour_date)
        elif s_from_date:
            from_date = date.fromisoformat(s_from_date)
            from_date -= timedelta(days=1)

            orders = Order.query.filter(Order.tour_date >= from_date)
        elif s_by_date:
            by_date = date.fromisoformat(s_by_date)
            by_date += timedelta(days=1)

            orders = Order.query.filter(by_date >= Order.tour_date)
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


"""
def get_tours(filters):
    if filters:
        str_from_price = filters.get('from_price', None)
        str_by_price = filters.get('by_price', None)

        if not str_by_price:
            str_by_price = 10e10

        if not str_from_price:
            str_from_price = '0'

        from_price = float(str_from_price) - 1
        by_price = float(str_by_price) + 1

        if from_price and by_price:
            tours = Tour.query.filter(Tour.day_cost > int(from_price)).filter(by_price > Tour.day_cost)
        elif from_price:
            tours = Tour.query.filter(Tour.day_cost >= from_price)
        elif by_price:
            tours = Tour.query.filter(by_price >= Tour.day_cost)
        else:
            tours = Tour.query.all()
    else:
        tours = Tour.query.all()

    return list(tours)
"""

