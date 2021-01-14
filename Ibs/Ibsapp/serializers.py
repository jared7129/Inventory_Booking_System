from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Member
        fields = ('name','surname','date_joined', 'booking_count',)


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Inventory
        fields = ('id_no','title','description', 'remaining_count', 'expiration_date',)

class BookingSerializer(serializers.ModelSerializer):
    member=MemberSerializer
    inventory=InventorySerializer
    class Meta:
        model= Booking
        fields =('member','inventory','booking_date','is_active',)
