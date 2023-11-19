from rest_framework import serializers
from bank_accounts.serializers import BankAccountSerializer
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    bank_account = BankAccountSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "city", "phone_number", "bank_account"]


class PublicUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["name", "phone_number"]

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name[0]}."


class AdminUserSerializer(PublicUserSerializer):
    class Meta:
        model = User
        fields = ["email", "phone_number", "name", "city", "last_login"]
