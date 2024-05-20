from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Deposit, Saving

# Create your models here.
class User(AbstractUser):
    opn_deposits = models.ManyToManyField(Deposit, related_name='opn_deposit_users', through='OpenDeposit')
    opn_savings = models.ManyToManyField(Saving, related_name='opn_saving_users', through='OpenSaving')
    nickname = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    age = models.IntegerField()
    job = models.TextField()
    income = models.IntegerField()

class OpenDeposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    balance = models.IntegerField()

class OpenSaving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE)
    balance = models.IntegerField()