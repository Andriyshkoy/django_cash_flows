import django_filters

from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    """Provide search and range filtering for transactions."""

    created_at = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.DateRangeWidget(attrs={"type": "date"})
    )

    class Meta:
        model = Transaction
        fields = ["created_at", "status", "tx_type", "category", "sub_category"]
