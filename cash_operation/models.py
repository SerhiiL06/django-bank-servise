from django.db import models

from django.core.validators import MaxValueValidator
from bank_accounts.models import BankCard


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

    def __str__(self):
        type_of = "Refill" if self.type_of == "re" else "Withdrawal"
        return f"{self.card.bank_account.owner} amount {self.amount} | {type_of}"


class ElectronicOperation(Transaction):
    card = models.ForeignKey(
        BankCard, on_delete=models.PROTECT, related_name="send_operations"
    )
    recipient_card = models.ForeignKey(
        BankCard, on_delete=models.PROTECT, related_name="recepient_operation"
    )
    message = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Sender {self.card.bank_account.owner} amount {self.amount}"
