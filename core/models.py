from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from reference.models import Category, Status, SubCategory, TxType


class Transaction(models.Model):
    """Represents a single cash-flow transaction made by a user."""

    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions"
    )
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
        """Validate category relationships before saving.

        Ensures that the selected sub category belongs to the provided category
        and that the category is compatible with the chosen transaction type.
        """
        if self.sub_category.category_id != self.category_id:
            raise ValidationError("Sub category must belong to category")
        if self.category.tx_type_id != self.tx_type_id:
            raise ValidationError("Category must belong to transaction type")

    def save(self, *args, **kwargs):
        """Run full validation before persisting the instance."""
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("-created_at",)
        unique_together = (
            "user",
            "status",
            "tx_type",
            "category",
            "sub_category",
            "amount",
        )
        verbose_name = "Тransaction"
        verbose_name_plural = "Transactions"

    def __str__(self) -> str:
        """Return a readable representation of the transaction."""
        return f"{self.created_at} {self.amount}"
