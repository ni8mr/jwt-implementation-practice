from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserDetails(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone_no = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User)


class BankRegister(models.Model):
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    bank_account_no = models.IntegerField(blank=True, null=True)
    account_name = models.CharField(max_length=100, blank=True, null=True)
    account_phone_no = models.CharField(max_length=100, blank=True, null=True)
