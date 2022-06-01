
from ctypes import BigEndianStructure, addressof
from tkinter.filedialog import asksaveasfile
from django.db import models
from django.utils.translation import gettext_lazy as _


LAYER_HEIGHTS = ["0.1mm", "0.15mm", "0.2mm", "0.25mm", "0.3mm", "0.35mm", "0.4mm", "0.45mm", "0.5mm", "0.55mm", "0.6mm"]
NOZZLE_SIZES = ["0.25", "0.4", "0.8"]
MATERIAL_LIST = []
INFILL_TYPES = []
INFILL_DENSITIES = []


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

    order_id models.AutoField(primary_key=True)D
    print_id = 
    order status
    buyer_id = 
    seller_id = 
    seller_address:
    buyer_address:
    buyer payment information
    seller payment information
    shipping tracking
    confirmation photos
    buyer photo approval

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




    class nozzleSizes(models.TextChoices):
        SML = "0.25mm"
        MED = "0.4mm"
        LRG = "0.8mm"
    
    nozzle_size  = models.TextField(
        choices = NOZZLE_SIZES,
        default = nozzleSizes.MED
    )

    modelLink = models.URLField()
    modelName = models.TextField()
    modelLink = models.TextField()

    printHeight = models.TextChoices(LAYER_HEIGHTS)