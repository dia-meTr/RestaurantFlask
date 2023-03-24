from wtforms import StringField, FloatField, DateField, SelectField, IntegerField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

from datetime import datetime



class AddEditOrderForm(FlaskForm):
    waiter = SelectField('Waiter', choices=[], validators=[DataRequired()], validate_choice=False)
    status = SelectField('Order Status', choices=[], validators=[DataRequired()], validate_choice=False)
    table = IntegerField('Table', validators=[DataRequired()], default=7)
    orders_date = DateField('Order date', validators=[DataRequired()], default=datetime.now())
    submit = SubmitField('')
