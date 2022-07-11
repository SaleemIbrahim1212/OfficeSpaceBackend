from rest_framework import serializers
from .models import BookingSpace

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookingSpace
        fields = '__all__'