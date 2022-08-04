from rest_framework import generics
from client.models import *
from client.serializers import *
from rest_framework.decorators import api_view
from helpers.utils import *


@api_view(['GET', 'POST'])
def client_list_view(request):

    if request.method == 'GET':
        try:
            data = Client.objects.all()
            ser = ClientGetSerializer(data, many=True)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'POST':
        try:
            ser = ClientCreateSerializer(data=request.data)
            if ser.is_valid():
                instance = ser.save()
                result = ClientGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Something wrong with the input data')
        except Exception as e:
            return response_failed(e.args)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail_view(request, pk):

    if request.method == 'GET':
        try:
            data = Client.objects.get(pk=pk)
            ser = ClientGetSerializer(data)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)

    elif request.method == 'PUT':
        try:
            current_obj = Client.objects.get(pk=pk)
            new_obj = request.data
            ser = ClientCreateSerializer(current_obj, data=new_obj, partial=True)
            if ser.is_valid():
                instance = ser.save()
                result = ClientGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Serializer not valid')
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'DELETE':
        try:
            current_obj = Client.objects.get(pk=pk)
            current_obj.delete()
            return response_success({'message':'Restaurant was deleted!'})
        except Exception as e:
            return response_failed('Was not possible to delete this restaurant, maybe the ID informed doesnt exist')
