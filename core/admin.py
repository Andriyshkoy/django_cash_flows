from django.contrib import admin

from .forms import TransactionAdminForm
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Admin interface for :class:`Transaction` objects."""

    form = TransactionAdminForm
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
