from logging import NOTSET
from xml.dom.xmlbuilder import _DOMInputSourceStringDataType
from django.db import models
from django.utils.translation import gettext_lazy as _
from numpy import size

LAYER_HEIGHTS = ["0.1mm", "0.15mm", "0.2mm", "0.25mm", "0.3mm", "0.35mm", "0.4mm", "0.45mm", "0.5mm", "0.55mm", "0.6mm"]
NOZZLE_SIZES = ["0.25", "0.4", "0.8"]


class Order(models.Model):

    print info:
    print model
    printer type
    nozzle size
    layer height
    infill type
    infill density
    post processing requirement and notes

    order info:
    order status
    buyer ID:
    seller ID:
    return address:
    shipping address:
    buyer payment information
    seller payment information
    shipping tracking
    confirmation photos
    buyer photo approval
    




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