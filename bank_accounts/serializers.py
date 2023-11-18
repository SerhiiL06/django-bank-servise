from rest_framework.serializers import ModelSerializer
from .models import BankAccount, BankCard


class BankCardSerializer(ModelSerializer):
    class Meta:
        model = BankCard
        fields = "__all__"


class BankAccountSerializer(ModelSerializer):
    account = BankCardSerializer()

    class Meta:
        model = BankAccount
        fields = ["box_number", "account"]
