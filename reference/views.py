from rest_framework import viewsets

from .models import Category, Status, SubCategory, TxType
from .serializers import (
    CategorySerializer,
    StatusSerializer,
    SubCategorySerializer,
    TxTypeSerializer,
)


class StatusViewSet(viewsets.ModelViewSet):
    """API endpoint for managing statuses."""

    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TxTypeViewSet(viewsets.ModelViewSet):
    """API endpoint for managing transaction types."""

    queryset = TxType.objects.all()
    serializer_class = TxTypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for managing transaction categories."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        """Optionally filter categories by transaction type."""
        queryset = super().get_queryset()
        tx_type_id = self.request.query_params.get("tx_type")
        if tx_type_id:
            queryset = queryset.filter(tx_type_id=tx_type_id)
        return queryset


class SubCategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for managing sub categories."""

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        """Optionally filter sub categories by parent category."""

        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
