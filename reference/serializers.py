from rest_framework import serializers

from .models import Category, Status, SubCategory, TxType


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class TxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TxType
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
