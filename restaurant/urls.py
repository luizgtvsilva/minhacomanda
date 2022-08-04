from django.urls import path, include
from restaurant.views import *

urlpatterns = [
    path('restaurant/', restaurant_list_view),
    path('restaurant/<int:pk>', restaurant_detail_view)
]