from django.urls import path, include
from menu.views import *

urlpatterns = [
    path('menu/', menu_list_view),
    path('menu/<int:pk>', menu_detail_view),
]