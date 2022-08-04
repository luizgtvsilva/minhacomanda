from rest_framework import serializers
from client.serializers import *
from restaurant.serializers import *
from order.models import *

class OrderCreateSerializer(serializers.ModelSerializer):
    order_items = ItemGetSerializer(read_only=True, many=True)
    order_client = ClientGetSerializer(read_only=True)
    order_restaurant = RestaurantGetSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderGetSerializer(serializers.ModelSerializer):
    items = ItemGetSerializer(many=True)
    client = ClientGetSerializer()
    restaurant = RestaurantGetSerializer()

    class Meta:
        model = Order
        fields = '__all__'