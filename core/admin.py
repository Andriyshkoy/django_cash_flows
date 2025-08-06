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
        "user",
    )
    list_filter = ("status", "tx_type", "category", "sub_category", "user")
    search_fields = ("comment",)
    date_hierarchy = "created_at"
