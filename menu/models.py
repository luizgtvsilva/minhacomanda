from django.db import models
from item.models import *

class Menu (models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    items = models.ManyToManyField(Item, related_name='items_menu', blank=True)
