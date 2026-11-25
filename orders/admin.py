from django.contrib import admin
from orders.models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "status", "total", "created_at", "updated_at", "shipping_address"]
    list_filter = ["status", "created_at"]
    search_fields = ["id", "user", "status"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "product_title", "quantity", "price", "line_total"]
    list_filter = ["order__status"]
    search_fields = ["product_title", "order__id", "order__user__email"]
    readonly_fields = ["line_total"]


