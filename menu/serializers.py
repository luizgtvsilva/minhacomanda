from rest_framework import serializers
from menu.models import *
from item.serializers import *

class MenuCreateSerializer(serializers.ModelSerializer):
    items_menu = ItemGetSerializer(read_only=True, many=True)

    class Meta:
        model = Menu
        fields = '__all__'

class MenuGetSerializer(serializers.ModelSerializer):
    items = ItemGetSerializer(many=True)

    class Meta:
        model = Menu
        fields = '__all__'
