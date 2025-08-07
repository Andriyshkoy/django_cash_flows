from rest_framework import serializers

from .models import Category, Status, SubCategory, TxType


class StatusSerializer(serializers.ModelSerializer):
    """Serialize :class:`Status` objects for the API."""

    class Meta:
        model = Status
        fields = "__all__"


class TxTypeSerializer(serializers.ModelSerializer):
    """Serialize :class:`TxType` objects for the API."""

    class Meta:
        model = TxType
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """Serialize :class:`Category` objects for the API."""

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    """Serialize :class:`SubCategory` objects for the API."""

    class Meta:
        model = SubCategory
        fields = "__all__"
