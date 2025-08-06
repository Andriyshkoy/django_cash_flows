from rest_framework import viewsets

from .models import Category, Status, SubCategory, TxType
from .serializers import (
    CategorySerializer,
    StatusSerializer,
    SubCategorySerializer,
    TxTypeSerializer,
)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TxTypeViewSet(viewsets.ModelViewSet):
    queryset = TxType.objects.all()
    serializer_class = TxTypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        tx_type_id = self.request.query_params.get("tx_type")
        if tx_type_id:
            queryset = queryset.filter(tx_type_id=tx_type_id)
        return queryset


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
