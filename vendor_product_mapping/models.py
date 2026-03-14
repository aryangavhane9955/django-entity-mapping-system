from django.db import models
from vendor.models import Vendor
from product.models import Product

class VendorProductMapping(models.Model):

    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        unique_together = ['vendor','product']