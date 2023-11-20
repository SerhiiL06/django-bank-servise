from django.contrib import admin
from .models import TerminalOperation, ElectronicOperation


@admin.register(TerminalOperation)
class TepminalAdmin(admin.ModelAdmin):
    list_display = ["card", "date_operation"]
    fields = ["card", "amount", "date_operation", "type_of"]
    readonly_fields = fields
    list_per_page = 10


@admin.register(ElectronicOperation)
class ElectronicAdmin(admin.ModelAdmin):
    pass
