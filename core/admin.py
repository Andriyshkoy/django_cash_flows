from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "status",
        "tx_type",
        "category",
        "sub_category",
        "amount",
    )
    list_filter = ("status", "tx_type", "category", "sub_category")
    search_fields = ("comment",)
    date_hierarchy = "created_at"
