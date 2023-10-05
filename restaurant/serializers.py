from rest_framework import serializers
from restaurant.models import Menu, Booking

_ALL_FIELDS = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = _ALL_FIELDS



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = _ALL_FIELDS

