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


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
