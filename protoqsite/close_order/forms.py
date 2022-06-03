from django.forms import ModelForm
from close_order.models import User, Order

class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ["user_id"]

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ["order_id"]