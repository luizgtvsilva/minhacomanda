from django.urls import path, include
from item.views import *

urlpatterns = [
    path('item/', item_list_view),
    path('item/<int:pk>', item_detail_view)
]