from django.contrib import admin
from .models import BankAccount, BankCard

admin.site.register(BankAccount)
admin.site.register(BankCard)
