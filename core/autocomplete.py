from dal import autocomplete

from reference.models import Category, SubCategory


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    """Autocomplete for categories filtered by transaction type."""

    def get_queryset(self):
        """Return ordered categories optionally filtered by type."""
        qs = Category.objects.all()
        tx_type_id = self.forwarded.get("tx_type")
        if tx_type_id:
            qs = qs.filter(tx_type_id=tx_type_id)
        return qs.order_by("name")


class SubCategoryAutocomplete(autocomplete.Select2QuerySetView):
    """Autocomplete for subcategories filtered by category."""

    def get_queryset(self):
        """Return ordered subcategories optionally filtered by parent."""
        qs = SubCategory.objects.all()
        category_id = self.forwarded.get("category")
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs.order_by("name")
