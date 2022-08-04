from django.shortcuts import render
from rest_framework import status, generics
from item.models import *
from item.serializers import *
from rest_framework.decorators import api_view
from helpers.utils import *


@api_view(['GET', 'POST'])
def item_list_view(request):

    if request.method == 'GET':
        try:
            data = Item.objects.all()
            ser = ItemGetSerializer(data, many=True)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'POST':
        try:
            ser = ItemCreateSerializer(data=request.data)
            if ser.is_valid():
                instance = ser.save()
                result = ItemGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Something wrong with the input data')
        except Exception as e:
            return response_failed(e.args)


@api_view(['GET', 'PUT', 'DELETE'])
def item_detail_view(request, pk):

    if request.method == 'GET':
        try:
            data = Item.objects.get(pk=pk)
            ser = ItemGetSerializer(data)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)

    elif request.method == 'PUT':
        try:
            current_obj = Item.objects.get(pk=pk)
            new_obj = request.data
            ser = ItemCreateSerializer(current_obj, data=new_obj, partial=True)
            if ser.is_valid():
                instance = ser.save()
                result = ItemGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Serializer not valid')
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'DELETE':
        try:
            current_obj = Item.objects.get(pk=pk)
            current_obj.delete()
            return response_success({'message':'Restaurant was deleted!'})
        except Exception as e:
            return response_failed('Was not possible to delete this restaurant, maybe the ID informed doesnt exist')