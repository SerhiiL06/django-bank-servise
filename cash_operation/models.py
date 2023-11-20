from django.db import models
from django.core.validators import MaxValueValidator
from bank_accounts.models import BankCard, BankAccount


class Transaction(models.Model):
    date_operation = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MaxValueValidator(50_000)]
    )

    class Meta:
        abstract = True


class TerminalOperation(Transaction):
    terminal_id = models.PositiveIntegerField()
    card = models.ForeignKey(
        BankCard, on_delete=models.PROTECT, related_name="terminal_operations"
    )
    operatation_type = (
        ("re", "refill"),
        ("with", "withdrawal"),
    )

    type_of = models.CharField(choices=operatation_type, max_length=10)


class ElectronicOperation(Transaction):
    card = models.ForeignKey(
        BankCard, on_delete=models.PROTECT, related_name="send_oretations"
    )
    recipient_card = models.ForeignKey(
        BankCard, on_delete=models.PROTECT, related_name="recepient_operation"
    )
    message = models.CharField(max_length=150, blank=True, null=True)
