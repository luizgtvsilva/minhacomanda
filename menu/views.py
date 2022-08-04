from django.shortcuts import render
from rest_framework import status, generics
from menu.models import *
from menu.serializers import *
from rest_framework.decorators import api_view
from helpers.utils import *


@api_view(['GET', 'POST'])
def menu_list_view(request):

    if request.method == 'GET':
        try:
            data = Menu.objects.all()
            ser = MenuGetSerializer(data, many=True)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'POST':
        try:
            ser = MenuCreateSerializer(data=request.data)
            if ser.is_valid():
                instance = ser.save()
                result = MenuGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Something wrong with the input data')
        except Exception as e:
            return response_failed(e.args)


@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail_view(request, pk):

    if request.method == 'GET':
        try:
            data = Menu.objects.get(pk=pk)
            ser = MenuGetSerializer(data)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)

    elif request.method == 'PUT':
        try:
            current_obj = Menu.objects.get(pk=pk)
            new_obj = request.data
            ser = MenuCreateSerializer(current_obj, data=new_obj, partial=True)
            if ser.is_valid():
                instance = ser.save()
                result = MenuGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Serializer not valid')
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'DELETE':
        try:
            current_obj = Menu.objects.get(pk=pk)
            current_obj.delete()
            return response_success({'message':'Menu was deleted!'})
        except Exception as e:
            return response_failed('Was not possible to delete this menu, maybe the ID informed doesnt exist')
