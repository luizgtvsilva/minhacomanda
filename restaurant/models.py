from django.db import models
from menu.models import *

class Restaurant (models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    menus = models.ManyToManyField(Menu, related_name='restaurant_menu', blank=True)