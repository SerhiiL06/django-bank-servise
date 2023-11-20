from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from django.shortcuts import get_object_or_404
from .logic import withdrawal_cash, refill_cash, check_exists_cards
from bank_accounts.models import BankCard
from .serializers import TerminalOperationSerializer, ElectronicOperationSerializer


class RefillAndWithdrawalCash(APIView):
    http_method_names = ["post"]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = TerminalOperationSerializer(data=request.data, many=False)
        data.is_valid(raise_exception=True)
        card = get_object_or_404(BankCard, id=data.validated_data["card"])

        if card and card.available:
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
        if check_relust:
            sender, recipient = check_relust

            if sender.bank_account.owner == request.user:
                if sender.balance >= amount:
                    sender.balance -= amount

                    recipient.balance += amount

                    sender.save()
                    recipient.save()

                    data.save(card=sender, recipient_card=recipient)

        return Response(status=204)
