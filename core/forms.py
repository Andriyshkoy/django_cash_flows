from django import forms

from reference.models import Category, SubCategory

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "status",
            "tx_type",
            "category",
            "sub_category",
            "amount",
            "comment",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tx_type_id = self["tx_type"].value() or self.initial.get("tx_type")
        category_id = self["category"].value() or self.initial.get("category")

        if tx_type_id:
            self.fields["category"].queryset = Category.objects.filter(
                tx_type_id=tx_type_id
            )
        else:
            self.fields["category"].queryset = Category.objects.none()

        if category_id:
            self.fields["sub_category"].queryset = SubCategory.objects.filter(
                category_id=category_id
            )
        else:
            self.fields["sub_category"].queryset = SubCategory.objects.none()

    class Media:
        js = ["core/transaction_form.js"]
