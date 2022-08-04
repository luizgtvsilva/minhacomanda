from django.urls import path, include
from order.views import *

urlpatterns = [
    path('order/', order_list_view),
    path('order/<int:pk>', order_detail_view),
]