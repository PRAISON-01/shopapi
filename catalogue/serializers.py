from rest_framework import serializers
from .models import Product, Category, Cart, CartItem, Review

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'is_active', 'description', 'sku', 'category']



class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only = True)

    class Meta:
        model = Category
        fields = ['name', 'id', 'products']



class CartItemSerializer(serializers.ModelSerializer):
    product  = ProductSerializer()
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_price']

    def get_total_price(self, item: CartItem):
        return item.product.price * item.quantity

class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['cart_id', 'items', 'total_price']

    def get_total_price(self, items):
        total = 0
        for item in items.items.all():
            total += item.product.price * item.quantity
        return total

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        read_only_fields = ['product', 'user']
        fields = ['product', 'user', 'rating', 'comment']

    def create(self, validated_data):
        product_id = self.context['product']
        user = self.context['user']
        return Review.objects.create(user=user, product_id=product_id, **validated_data)



"""
Difference between serializers and Model Serializers
    Model Serializers allows you to base the validations and constraints based off existing models allows for reusablilty
    Serializers makes you write the validation evn if you have written it for the model before
    
    NOTE: 
    One of the major reason for a Serializer is with the aim of not displaying all your fields (configuration)
"""