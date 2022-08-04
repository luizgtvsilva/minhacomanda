from rest_framework.decorators import api_view
from helpers.utils import *
from order.models import *
from order.serializers import *


@api_view(['GET', 'POST'])
def order_list_view(request):

    if request.method == 'GET':
        try:
            data = Order.objects.all()
            ser = OrderGetSerializer(data, many=True)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'POST':
        try:
            ser = OrderCreateSerializer(data=request.data)
            if ser.is_valid():
                instance = ser.save()
                result = OrderGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Something wrong with the input data')
        except Exception as e:
            return response_failed(e.args)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail_view(request, pk):

    if request.method == 'GET':
        try:
            data = Order.objects.get(pk=pk)
            ser = OrderGetSerializer(data)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)

    elif request.method == 'PUT':
        try:
            current_obj = Order.objects.get(pk=pk)
            new_obj = request.data
            ser = OrderCreateSerializer(current_obj, data=new_obj, partial=True)
            if ser.is_valid():
                instance = ser.save()
                result = OrderGetSerializer(instance).data
                return response_success(data=result)
            else:
                return response_failed('Serializer not valid')
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'DELETE':
        try:
            current_obj = Order.objects.get(pk=pk)
            current_obj.delete()
            return response_success({'message':'Menu was deleted!'})
        except Exception as e:
            return response_failed('Was not possible to delete this menu, maybe the ID informed doesnt exist')

