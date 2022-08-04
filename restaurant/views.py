from django.shortcuts import render
from rest_framework import status, generics
from restaurant.models import *
from restaurant.serializers import *
from rest_framework.decorators import api_view
from helpers.utils import *


@api_view(['GET', 'POST'])
def restaurant_list_view(request):

    if request.method == 'GET':
        try:
            data = Restaurant.objects.all()
            ser = RestaurantGetSerializer(data, many=True)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'POST':
        try:
            ser = RestaurantCreateSerializer(data=request.data)
            if ser.is_valid():
                instance = ser.save()
                result = RestaurantGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Something wrong with the input data')
        except Exception as e:
            return response_failed(e.args)


@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail_view(request, pk):

    if request.method == 'GET':
        try:
            data = Restaurant.objects.get(pk=pk)
            ser = RestaurantGetSerializer(data)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)

    elif request.method == 'PUT':
        try:
            current_obj = Restaurant.objects.get(pk=pk)
            new_obj = request.data
            ser = RestaurantCreateSerializer(current_obj, data=new_obj, partial=True)
            if ser.is_valid():
                instance = ser.save()
                result = RestaurantGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Serializer not valid')
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'DELETE':
        try:
            current_obj = Restaurant.objects.get(pk=pk)
            current_obj.delete()
            return response_success({'message':'Restaurant was deleted!'})
        except Exception as e:
            return response_failed('Was not possible to delete this restaurant, maybe the ID informed doesnt exist')
