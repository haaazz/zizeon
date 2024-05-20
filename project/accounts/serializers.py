from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, allow_blank=False)
    gender = serializers.CharField(required=True, allow_blank=False)
    age = serializers.IntegerField(required=True)
    job = serializers.CharField(required=True, allow_blank=False)
    income = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'gender': self.validated_data.get('gender', ''),
            'age': self.validated_data.get('age', 0),
            'job': self.validated_data.get('job', ''),
            'income': self.validated_data.get('income', 0),
        }