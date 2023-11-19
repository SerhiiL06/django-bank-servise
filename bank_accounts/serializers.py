from rest_framework import serializers
from .models import BankAccount, BankCard


class BankCardSerializer(serializers.ModelSerializer):
    card_number = serializers.SerializerMethodField()

    class Meta:
        model = BankCard
        fields = ["card_number", "balance", "card_type", "available"]

    def get_card_number(self, obj):
        hashed_card = "*" * 12 + str(obj.card_number)[12:]
        return hashed_card


class BankAccountSerializer(serializers.ModelSerializer):
    cards = BankCardSerializer(many=True, read_only=True)

    class Meta:
        model = BankAccount
        fields = ["box_number", "cards"]
