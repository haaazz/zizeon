from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import OpenDeposit, OpenSaving

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

UserModel = get_user_model()
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'gender'):
            extra_fields.append('gender')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'job'):
            extra_fields.append('job')
        if hasattr(UserModel, 'income'):
            extra_fields.append('income')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)

class OpenDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenDeposit
        fields = '__all__'
        read_only_fields = ('user', 'deposit',)

class OpenSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenSaving
        fields = '__all__'
        read_only_fields = ('user', 'saving',)

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'