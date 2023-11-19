from .models import BankCard
from random import randrange


def create_correct_number():
    while True:
        card_number = "".join([str(randrange(10)) for _ in range(16)])
        if not BankCard.objects.filter(card_number=card_number).exists():
            break

    new_list = []
    for num in list(card_number):
        if len(new_list) in (4, 9, 14):
            new_list.append("-")
        new_list.append(num)

    return "".join(new_list)
