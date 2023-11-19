from django.contrib import admin
from .models import BankAccount, BankCard
from .inlines import BankCardInline


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ["owner", "status"]
    fields = ["owner", "box_number", "status"]
    readonly_fields = ["owner", "box_number"]

    search_fields = ["owner__first_name", "owner__last_name", "box_number"]
    ordering = ["owner"]
    list_filter = ["status"]

    inlines = [BankCardInline]


@admin.register(BankCard)
class BankCardAdmin(admin.ModelAdmin):
    list_display = ["card_number"]
    fields = ["bank_account", "balance", "card_number", "ccv_code"]
    readonly_fields = fields
