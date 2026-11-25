from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import ProductViewSet, get_product_by_category, CartViewSet, ReviewViewSet

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')

router.register('carts',CartViewSet, basename='carts')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')

product_router.register('reviews', ReviewViewSet, basename='product-reviews')


urlpatterns = [
    path('', include(router.urls)),
    path('categories/<slug:slug>/', get_product_by_category, name='product_list_by_category'),
    path('', include(product_router.urls))
]

urlpatterns += router.urls
# api/v1/**

# urlpatterns = [
#     path('products/', product_list, name='product_list'),
#     path('categories/', views.CategoryListView.as_view(), name='category_list'),
#     path('categories/<slug:slug>', get_product_by_category, name='get_product_by_category')
# ]


#
# urlpatterns = [
#     path('products', product_list, name='product_list'),
#     path('product/<pk:int>', .as_view(), name='category_list'),
#     path('categories/<slug:slug>/', get_product_by_category, name='product_list_by_category'),
# ]
# For class Based View
#     path('products', ProductListView.as_view(), name='product_list')