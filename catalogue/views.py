from django.shortcuts import render, get_object_or_404
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .serializers import ProductSerializer, CategorySerializer, CartSerializer, ProductReviewSerializer
from .models import Product, Category, Cart, Review


# Create your views here.

# Function based View
@api_view(['GET'])
def product_list(request):
    queryset = Product.objects.all().filter(is_active=True)
    okay = ProductSerializer(queryset, many=True)
    return Response(okay.data, status=status.HTTP_200_OK)


# Class Based View
class ProductViewSet(ModelViewSet) :
    queryset = Product.objects.all().filter(is_active=True)
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAdminUser()]
#
# class ProductDetailView(RetrieveAPIView):
#     queryset = Product.objects.all().filter(is_active=True)
#     serializer_class = CategorySerializer
#     permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_by_category(request, slug):
    queryset = get_object_or_404(Category, slug=slug)
    serializer = CategorySerializer(queryset)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CartViewSet(CreateModelMixin, RetrieveAPIView, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


class ReviewViewSet(ModelViewSet):
    serializer_class = ProductReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_context(self):
        return {'user': self.request.user, 'product' : self.kwargs['product_pk'],}


# class CategoryListView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#     def get_queryset(self, slug):
#         Category.objects.get(slug=slug)



# Class Based View
# Function Based View3
# URL Configuration in django