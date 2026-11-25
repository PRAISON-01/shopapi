from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Order, OrderItem
from .serializers import OrderSerializers, OrderItemSerializer


# Create your views here.


class OrderApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderItemApiView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
