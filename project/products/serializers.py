from rest_framework import serializers
from .models import Deposit, DepositOption, Saving, SavingOption

class DepositsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('deposit',)

class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('saving',)