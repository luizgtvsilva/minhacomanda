from tkinter import CASCADE
from django.db import models
from client.models import *
from restaurant.models import *
from item.models import *


class Order(models.Model):
    client = models.ForeignKey(Client, related_name='order_client', blank=False, null=False, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, related_name='order_restaurant', blank=False, null=False, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='order_items', blank=True)
    total_value = models.FloatField()