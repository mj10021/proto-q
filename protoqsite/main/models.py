from distutils.text_file import TextFile
from django.db import models
from django.forms import CharField, EmailField, IntegerField

LAYER_HEIGHTS = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
NOZZLE_SIZES = [0.25, 0.4, 0.8]
MATERIAL_LIST = ["PLA", "PETG"]
INFILL_TYPES = ["Grid"]
INFILL_DENSITIES = [range(0,101,1)]
ORDER_STATUS_OPTS = ["Awaiting shipping", "awaiting confirm..."]
SHIPPING_OPTIONS = []
LEAD_TIMES = []


class Print(models.Model):

    print_id = models.AutoField(primary_key=True)
    print_model = models.URLField()
    printer_type = models.CharField(
        max_length = 10,
        choices = ["FDM", "SLA", "SLS"],
        default = "FDM",
    )
    print_material = models.CharField(
        max_length = 100,
        choices = MATERIAL_LIST,
        default = "PETG",
    )
    nozzle_size = models.DecimalField(
        max_digits = 3, 
        decimal_places=2, 
        choices=NOZZLE_SIZES,
    )
    layer_height = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        choices=LAYER_HEIGHTS,
    )
    infill_type = models.CharField(
        max_length=20,
        choices=INFILL_TYPES
    )
    infill_density = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        choices=INFILL_DENSITIES,
    )
    processing_required = models.BooleanField()
    processing_notes = models.TextField()

    def __str__(self):
        return self.print_id

class Ticket(models.Model):#open order

    ticket_id = models.AutoField(primary_key=True)
    buy_or_sell = models.BooleanField()
    ticket_moq = models.IntegerField(max_length=1000)
    ticket__available_qty = models.IntegerField(max_length=1000)
    ticket_qty_filled = models.IntegerField(max_length=1000)
    partial_fill_allowed = models.BooleanField()
    order_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )
    
    print_id = models.IntegerField()
    def __str__(self):
        return self.order_id

    shipping_options = models.CharField(max_length=1000, options=SHIPPING_OPTIONS)
    lead_times = models.charField(max_length=1000, options=LEAD_TIMES)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_qty = models.IntegerField(max_length=1000, default=1)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_OPTS)

    buyer_id = models.IntegerField()
    seller_id = models.IntegerField()

    from_address = models.TextField()
    to_address = models.TextField()

    payment_id = models.CharField(max_length=100)

    shipping_tracking = models.CharField(max_length=100)
    confirmation_photos = models.URLField()
    confirm_approval = models.BooleanField()





make a new class for purchases after the order is closed

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.EmailField()
    user_phone = models.IntegerField(max_length=20)
    open_bids = models.IntegerField(max_length=1000000)
    closed_bids = models.IntegerField(max_length=1000000)
    open_asks = models.IntegerField(max_length=1000000)
    closed_asks = models.IntegerField(max_length=1000000)

    def __str__(self):
        return self.user_id