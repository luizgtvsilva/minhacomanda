from rest_framework import serializers
from restaurant.models import *
from menu.serializers import *


class RestaurantCreateSerializer(serializers.ModelSerializer):
    restaurant_menu = MenuGetSerializer(read_only=True, many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantGetSerializer(serializers.ModelSerializer):
    menus = MenuGetSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
