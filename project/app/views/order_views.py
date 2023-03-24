import requests
from flask import render_template, redirect, url_for, request
from flask.views import MethodView

from app import app, db, BASE
from app.views.form import AddEditOrderForm
from app.models import Waiter, Status, Order



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


class AddOrderView(MethodView):
    def get(self):
        return render_template('add_edit_forms/add-edit_order.html', **self.prepare_context())

    def post(self):
        form = AddEditOrderForm()

        if form.validate_on_submit():
            requests.post(BASE + 'json_orders', json={
                'waiter_id': form.waiter.data.split()[0],
                'status_id': form.status.data.split()[0],
                'table': form.table.data
            })

        return redirect(url_for('get_all_orders'))

    def prepare_context(self):
        form = AddEditOrderForm()

        waiters = Waiter.query.all()
        form.waiter.choices = list(
            f'{waiter.id} - {waiter.first_name} {waiter.last_name}' for waiter in waiters
        )

        statuses = Status.query.all()
        form.status.choices = list(
            f'{status.id} - {status.status}' for status in statuses
        )

        title = 'ADD ORDER'
        submit_url = '/add-order'
        cancel_button = 'get_all_orders'

        return {
            'title': title,
            'form': form,
            'submit_url': submit_url,
            'cancel_button': cancel_button
        }


class EditOrderView(MethodView):
    def get(self, id):
        order = Order.query.get(id)

        return render_template('add_edit_forms/add-edit_order.html', **self.prepare_context(order))

    def post(self, id):
        order = requests.put(BASE + 'json_orders/' + str(id))
        if not order:
            return redirect(url_for('get_all_orders'))

        form = AddEditOrderForm()
        if form.validate_on_submit():
            requests.put(BASE + 'json_orders/' + str(id), json={
                'waiter_id': form.waiter.data.split()[0],
                'status_id': form.status.data.split()[0],
                'table': form.table.data
            })

            db.session.commit()

        return redirect(url_for('get_all_orders'))

    def prepare_context(self, order):
        form = AddEditOrderForm()

        waiters = Waiter.query.all()
        cur_waiter = Waiter.query.get(order.waiter_id)
        form.waiter.choices = [f'{cur_waiter.id} - {cur_waiter.first_name} {cur_waiter.last_name}'] + list(
            f'{waiter.id} - {waiter.first_name} {waiter.last_name}' for waiter in waiters if waiter.id != cur_waiter.id
        )

        statuses = Status.query.all()
        cur_status = Status.query.get(order.status_id)
        form.status.choices = [f'{cur_status.id} - {cur_status.status}'] + list(
            f'{status.id} - {status.status}' for status in statuses if status.id != cur_status.id
        )

        form.table.data = order.table

        submit_url = '/edit-order/' + str(order.id)
        cancel_button = 'get_all_orders'

        return {
            'form': form,
            'title': 'EDIT ORDER',
            'submit_url': submit_url,
            'cancel_button': cancel_button
        }


class DeleteOrderView(MethodView):
    def post(self, id):
        requests.delete(BASE + 'json_orders/' + f'{id}')

        return redirect(url_for('get_all_orders'))


app.add_url_rule('/orders', view_func=GetAllOrdersView.as_view('get_all_orders'), methods=['GET', 'POST'])
app.add_url_rule('/add-order', view_func=AddOrderView.as_view('add_order'), methods=['GET', 'POST'])
app.add_url_rule('/delete-order/<int:id>', view_func=DeleteOrderView.as_view('delete_order'), methods=['POST'])
app.add_url_rule('/edit-order/<int:id>', view_func=EditOrderView.as_view('edit_order'), methods=['POST', 'GET'])
