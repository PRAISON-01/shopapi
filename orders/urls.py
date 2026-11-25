from django.urls import path
from orders.views import OrderApiView, OrderItemApiView

urlpatterns = [
    path('orders/', OrderApiView.as_view(), name='order_list'),
    path('OrderItem/', OrderItemApiView.as_view(), name='order_item_list')
]