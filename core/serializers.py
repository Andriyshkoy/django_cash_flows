from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    def validate(self, attrs):
        sub_category = attrs["sub_category"]
        category = attrs["category"]
        tx_type = attrs["tx_type"]
        if sub_category.category_id != category.id:
            raise serializers.ValidationError("Sub category must belong to category")
        if category.tx_type_id != tx_type.id:
            raise serializers.ValidationError(
                "Category must belong to transaction type"
            )
        return attrs
