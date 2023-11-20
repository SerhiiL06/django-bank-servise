from rest_framework.response import Response
from bank_accounts.models import BankCard


def withdrawal_cash(card, ccv_code, data):
    if card.ccv_code == ccv_code:
        amount = data.validated_data["amount"]
        if card.balance >= amount:
            card.balance -= amount
            card.save()
            data.save(card=card)
            return Response(f"Thank you for you work!", status=202)

    return Response("Something went wrong!", status=400)


def refill_cash(card, data):
    card.balance += data.validated_data["amount"]
    card.save()
    data.save(card=card)
    return Response(f"You are correctly refill card!", status=202)


def check_exists_cards(card_1, card_2):
    sender_card = BankCard.objects.get(card_number=card_1)
    recipient_card = BankCard.objects.get(card_number=card_2)

    result = bool(sender_card and recipient_card)
    if result:
        return [sender_card, recipient_card]
