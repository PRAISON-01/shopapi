from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import RegisterSerializer, AddressSerializer
from .models import User, Address
from . import services

# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class AddressViewSet(ModelViewSet):
   serializer_class = AddressSerializer
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
       return Address.objects.filter(user=self.request.user).order_by('is_default')

   def perform_create(self, serializer):
       services.save_address(serializer, self.request.user)

   def perform_update(self, serializer):
       services.save_address(serializer, self.request.user)



