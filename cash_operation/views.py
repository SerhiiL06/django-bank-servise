from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import TerminalOperation, ElectronicOperation
from django.shortcuts import get_object_or_404
from bank_accounts.models import BankCard
from .serializers import TerminalOperationSerializer


class RefillAndWithdrawalCash(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = TerminalOperationSerializer(data=request.data, many=False)
        data.is_valid(raise_exception=True)
        card = get_object_or_404(BankCard, id=data.validated_data["card"])

        data.save(card=card)

        if card and card.available:
            if data.validated_data["type_of"] == "re":
                card.balance += data.validated_data["amount"]
                card.save()

                return Response(f"You are correctly refill card!", status=202)

            else:
                if card.ccv_code == request.data["ccv_code"]:
                    card.balance -= data.validated_data["amount"]
                    card.save()
                    return Response(f"Thank you for you work!", status=202)

                return Response("Your code is wrong!", status=400)

        return Response(status=204)


class MoneyTransfer(generics.CreateAPIView):
    pass
