from rest_framework import serializers
from .models import User, Address

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'first_name', 'last_name', 'is_active']

        readonly_fields = ['id', 'username']



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['email', 'phone', 'first_name', 'last_name', 'password', 'username']
        read_only_fields = ['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['user']
        # fields = ['user', 'label', 'recipient_name',  'address_one', 'address_two', 'city', 'state', 'country', 'postal_code', 'is_default']
        read_only = ['user']

