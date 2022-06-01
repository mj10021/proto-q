from django.db import models
from django.forms import IntegerField

LAYER_HEIGHTS = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
NOZZLE_SIZES = [0.25, 0.4, 0.8]
MATERIAL_LIST = ["PLA", "PETG"]
INFILL_TYPES = ["Grid"]
INFILL_DENSITIES = [range(0,101,1)]
ORDER_STATUS_OPTS = ["Awaiting shipping", "awaiting confirm..."]


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

class Order(models.Model):

    order_id = models.AutoField(primary_key=True)
    order_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )
    order_qty = models.IntegerField(max_length=1000, default=1)
    print_id = models.IntegerField()
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_OPTS)
    buyer_id = models.IntegerField()
    seller_id = models.IntegerField()
    """seller_address:
    buyer_address:
    buyer payment information
    seller payment information"""
    shipping_tracking = models.CharField(max_length=100)
    confirmation_photos = models.URLField()
    confirm_approval = models.BooleanField()


make a new class for purchases after the order is closed

class Buyer(models.Model):
    buyer_id= models.AutoField(primary_key=True)
    buyer_email
    buyer_phone
    buyer address
    open bids
    closed bids
    feedback

class Seller(models.Model):
    seller_id= models.AutoField(primary_key=True)
    seller_email
    seller_address
    seller_phone
    open asks
    closed asks
    feedback