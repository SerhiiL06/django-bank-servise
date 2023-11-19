from .models import TerminalOperation
from bank_accounts.models import BankCard
from rest_framework import serializers


class TerminalOperationSerializer(serializers.ModelSerializer):
    card = serializers.IntegerField(required=False)

    class Meta:
        model = TerminalOperation
        fields = ["terminal_id", "card", "type_of", "amount"]
