from django.core.exceptions import ValidationError
from django.db import models

from reference.models import Category, Status, SubCategory, TxType


class Transaction(models.Model):
    created_at = models.DateField(auto_now_add=True)
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, related_name="transactions"
    )
    tx_type = models.ForeignKey(
        TxType, on_delete=models.PROTECT, related_name="transactions"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="transactions"
    )
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.PROTECT, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)

    def clean(self):
        if self.sub_category.category_id != self.category_id:
            raise ValidationError("Sub category must belong to category")
        if self.category.tx_type_id != self.tx_type_id:
            raise ValidationError("Category must belong to transaction type")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.created_at} {self.amount}"
