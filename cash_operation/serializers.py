from .models import TerminalOperation, ElectronicOperation
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


class TransactionSerializer(serializers.Serializer):
    date_operation = serializers.SerializerMethodField()
    amount = serializers.FloatField(required=False)

    def get_date_operation(self, obj):
        return obj.date_operation.date()

    class Meta:
        abstract = True
        fields = ["id", "date_operation", "amount"]


class AllOperationsSerializer(TransactionSerializer):
    terminal_id = serializers.IntegerField(required=False)
    card = serializers.CharField()
    method_operation = serializers.SerializerMethodField()

    def get_method_operation(self, obj):
        if obj.type_of in ["re", "with"]:
            return "Terminal"

        return "Electronic"
