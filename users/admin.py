from django.contrib import admin
from .models import User
from bank_accounts.inlines import BankAccountInline


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ["email", "city", "phone_number", "join_at"]
    readonly_fields = ["phone_number", "join_at"]
    inlines = [BankAccountInline]
