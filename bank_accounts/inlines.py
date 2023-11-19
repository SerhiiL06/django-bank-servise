from django.contrib import admin
from .models import BankAccount, BankCard


class BankAccountInline(admin.StackedInline):
    model = BankAccount
    fields = ["box_number", "status"]
    readonly_fields = ["box_number"]
    can_delete = False


class BankCardInline(admin.TabularInline):
    model = BankCard
    fields = ["card_number", "card_type", "available"]
    readonly_fields = ["card_number", "card_type"]
    can_delete = False
    extra = 0
