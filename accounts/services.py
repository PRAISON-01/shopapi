from django.db import transaction
from .models import Address

@transaction.atomic
def save_address(serializer, user) -> Address:
    current_address = serializer.instance
    data = serializer.validated_data

    if current_address is None:
        make_default = data.get('is_default', False) or not Address.objects.filter(user=user).exists()
    else:
        make_default = data.get('is_default', False)
    #
    # if make_default:
    #     other_address = Address.objects.create(user=user, is_default=True)
    #     if current_address is not None:
    #         other_address = other_address.objects.filter(user=user)