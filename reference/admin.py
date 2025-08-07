from django.contrib import admin

from .models import Category, Status, SubCategory, TxType


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Manage :class:`Status` entries in the admin panel."""

    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(TxType)
class TxTypeAdmin(admin.ModelAdmin):
    """Manage transaction type entries."""

    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for transaction categories."""

    list_display = ("id", "name", "tx_type")
    list_filter = ("tx_type",)
    search_fields = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Admin interface for transaction sub categories."""

    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)
