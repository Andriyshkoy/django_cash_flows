from dal import autocomplete

from reference.models import Category, SubCategory


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.all()
        tx_type_id = self.forwarded.get("tx_type")
        if tx_type_id:
            qs = qs.filter(tx_type_id=tx_type_id)
        return qs.order_by("name")


class SubCategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SubCategory.objects.all()
        category_id = self.forwarded.get("category")
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs.order_by("name")
