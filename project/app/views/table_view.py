from datetime import date, timedelta

import requests
from flask import render_template, request
from flask.views import MethodView

from app import app
from app.models import Order
# from app.tests.test_clients_api import BASE

BASE = 'http://127.0.0.1:5000/'


# Get All Entities
class GetAllOrdersView(MethodView):
    def get(self):
        return render_template('tables/orders.html', **self.prepare_context(request.args))

    @staticmethod
    def prepare_context(filters=None):
        title = 'Orders'
        add_button = 'add_order'

        if not filters:
            data = requests.get(BASE + 'json_orders')
        else:
            data = requests.get(BASE + 'json_orders' + '?' + request.url.split('?')[-1])

        return {
            'title': title,
            'add_button': add_button,
            'orders': data.json(),
            'sort_from': filters.get('tour_date_from', None),
            'sort_by': filters.get('tour_date_by', None)
        }


app.add_url_rule('/orders', view_func=GetAllOrdersView.as_view('get_all_orders'), methods=['GET', 'POST'])
