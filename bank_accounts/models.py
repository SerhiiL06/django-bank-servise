from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator
from .validators import DateValidator, CardNumberValidator


class BankAccount(models.Model):
    ACCOUNT_STATUSES = (
        ("active", "active"),
        ("freeze", "freeze"),
        ("block", "block"),
    )

    owner = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name="bank_account"
    )
    box_number = models.UUIDField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=ACCOUNT_STATUSES, max_length=10, default="active")

    def __str__(self) -> str:
        return self.owner


class BankCard(models.Model):
    TYPE_OF_CARD = (
        ("debit", "debit"),
        ("credit", "credit"),
    )

    bank_account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE, related_name="cards"
    )
    balance = models.PositiveIntegerField(default=0)
    card_number = models.IntegerField(validators=[CardNumberValidator()])
    expiration_date = models.CharField(max_length=7, validators=[DateValidator()])
    ccv_code = models.IntegerField(validators=[MaxValueValidator(999)])
    card_type = models.CharField(choices=TYPE_OF_CARD, max_length=6)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.bank_account.owner
