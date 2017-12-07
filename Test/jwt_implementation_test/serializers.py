from .models import *
from rest_framework import serializers


class BankRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankRegister
        fields = ('bank_name', 'bank_account_no', 'account_name', 'account_phone_no')