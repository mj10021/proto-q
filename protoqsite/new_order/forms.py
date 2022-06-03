from django.forms import ModelFormfrom
from main.models import Print, Ticket, Order, User

class PrintForm(ModelForm):
    class Meta:
        model = Print
        fields = ["print_id", ]