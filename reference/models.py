from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class TxType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    tx_type = models.ForeignKey(
        TxType, on_delete=models.CASCADE, related_name="categories"
    )

    class Meta:
        unique_together = ("name", "tx_type")

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sub_categories"
    )

    class Meta:
        unique_together = ("name", "category")

    def __str__(self) -> str:
        return self.name
