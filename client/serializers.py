from rest_framework import serializers
from client.models import *
from drf_dynamic_fields import DynamicFieldsMixin


class ClientGetSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'