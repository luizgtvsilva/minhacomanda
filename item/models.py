from django.db import models

class Item (models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=250, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    time_to_prepare = models.TimeField(blank=True, null=True)