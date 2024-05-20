from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Deposit, Saving
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.
class User(AbstractUser):
    opn_deposits = models.ManyToManyField(Deposit, related_name='opn_deposit_users', through='OpenDeposit')
    opn_savings = models.ManyToManyField(Saving, related_name='opn_saving_users', through='OpenSaving')
    nickname = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    age = models.IntegerField(null=True, blank=True)
    job = models.TextField()
    income = models.IntegerField(null=True, blank=True)

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        gender = data.get("gender")
        age = data.get("age")
        job = data.get("job")
        income = data.get("income")

        user_email(user, email)
        user_username(user, username)

        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if gender:
            user_field(user, "gender", gender)
        if age:
            user.age = age
        if job:
            user_field(user, "job", job)
        if income:
            user.income = income
        
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)

        if commit:
            user.save()
        return user

class OpenDeposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    balance = models.IntegerField()

class OpenSaving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE)
    balance = models.IntegerField()