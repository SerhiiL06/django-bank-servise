from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import User
from .models import BankAccount, BankCard
import uuid

from random import choices, randrange
from datetime import datetime, timedelta


@receiver(post_save, sender=User)
def create_bank_account_and_card(instance, created, **kwargs):
    if created:
        # create account number

        # check if bank account is unique
        while True:
            box = uuid.uuid4()

            if not BankAccount.objects.filter(box_number=box).exists():
                break

        bank_account = BankAccount.objects.create(owner=instance, box_number=box)

        # create bank card

        while True:
            card_number = "".join((str(randrange(10)) for _ in range(16)))

            if not BankCard.objects.filter(card_number=card_number).exists():
                break

        expiration = datetime.now() + timedelta(days=1800)
        valid_date = f"{expiration.month}/{expiration.year}"
        ccv_code = int("".join((str(el) for el in choices(range(10), k=3))))
        BankCard.objects.create(
            bank_account=bank_account,
            card_number=card_number,
            expiration_date=valid_date,
            ccv_code=ccv_code,
            card_type="debit",
        )
