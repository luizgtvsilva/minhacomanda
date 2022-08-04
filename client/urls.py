from django.urls import path, include
from client.views import *

urlpatterns = [
    path('client/', client_list_view),
    path('client/<int:pk>', client_detail_view)
]