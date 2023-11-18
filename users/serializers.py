from rest_framework import serializers
from bank_accounts.serializers import BankAccountSerializer
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    bank_account = BankAccountSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "city", "phone_number", "bank_account"]
