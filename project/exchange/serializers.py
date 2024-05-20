from rest_framework import serializers
from .models import Exchange

class ExchangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'