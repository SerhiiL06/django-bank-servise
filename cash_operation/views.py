from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from django.db.models import Q, F, Value, CharField

from django.shortcuts import get_object_or_404
from .logic import withdrawal_cash, refill_cash, check_exists_cards
from bank_accounts.models import BankCard
from .serializers import (
    TerminalOperationSerializer,
    ElectronicOperationSerializer,
    AllOperationsSerializer,
)
from .models import TerminalOperation, ElectronicOperation


class RefillAndWithdrawalCash(APIView):
    http_method_names = ["post"]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = TerminalOperationSerializer(data=request.data, many=False)
        data.is_valid(raise_exception=True)
        card = get_object_or_404(BankCard, id=data.validated_data["card"])

        if not card or not card.available:
            return Response("Incorrect card", status=204)
        if data.validated_data["type_of"] == "re":
            return refill_cash(card=card, data=data)

        if data.validated_data["type_of"] == "with":
            ccv_code = request.data["ccv_code"]
            return withdrawal_cash(card=card, ccv_code=ccv_code, data=data)

        return Response(status=204)


class MoneyTransfer(APIView):
    http_method_names = ["post"]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = ElectronicOperationSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        sender_card = data.validated_data["card"]
        recipient_card = data.validated_data["recipient_card"]
        amount = data.validated_data["amount"]

        check_relust = check_exists_cards(card_1=sender_card, card_2=recipient_card)
        if not check_relust:
            return Response("One of card doesn't exists", status=204)

        sender, recipient = check_relust

        if sender.bank_account.owner != request.user:
            return Response("You canno't send money from another card", status=204)
        if not sender.balance >= amount:
            return Response(f"You don't have {amount} for this operation ", status=204)

        sender.balance -= amount

        recipient.balance += amount

        sender.save()
        recipient.save()

        data.save(card=sender, recipient_card=recipient)

        return Response(status=204)


class GetAllOperations(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        electronic = ElectronicOperation.objects.filter(
            Q(card__bank_account__owner=request.user)
        )
        terminal = TerminalOperation.objects.all()

        electronic.annotate(type_of=Value("", output_field=CharField()))

        union_query = terminal.union(electronic, all=True)

        serializer = AllOperationsSerializer(union_query, many=True)

        return Response(serializer.data, status=200)
