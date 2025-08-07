from django.db import models


class Status(models.Model):
    """Represent the processing status of a transaction."""

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
        ordering = ["name"]

    def __str__(self) -> str:
        """Return a readable representation of the status."""
        return self.name


class TxType(models.Model):
    """Represent a type of transaction (income or expense)."""

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Transaction Type"
        verbose_name_plural = "Transaction Types"
        ordering = ["name"]

    def __str__(self) -> str:
        """Return a readable representation of the transaction type."""
        return self.name


class Category(models.Model):
    """Group transactions of a specific type into logical buckets."""

    name = models.CharField(max_length=255, unique=True)
    tx_type = models.ForeignKey(
        TxType, on_delete=models.CASCADE, related_name="categories"
    )

    class Meta:
        unique_together = ("name", "tx_type")
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self) -> str:
        """Return a readable representation of the category."""
        return self.name


class SubCategory(models.Model):
    """Further classify transactions within a specific category."""

    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sub_categories"
    )

    class Meta:
        unique_together = ("name", "category")
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"
        ordering = ["name"]

    def __str__(self) -> str:
        """Return a readable representation of the sub category."""
        return self.name
