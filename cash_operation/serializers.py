from .models import TerminalOperation, ElectronicOperation
from bank_accounts.models import BankCard
from rest_framework import serializers


class TerminalOperationSerializer(serializers.ModelSerializer):
    card = serializers.IntegerField(required=False)

    class Meta:
        model = TerminalOperation
        fields = ["terminal_id", "card", "type_of", "amount"]


class ElectronicOperationSerializer(serializers.ModelSerializer):
    message = serializers.CharField(required=False)
    card = serializers.CharField(required=False)
    recipient_card = serializers.CharField(required=False)

    class Meta:
        model = ElectronicOperation
        fields = ["card", "amount", "recipient_card", "message"]
