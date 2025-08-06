import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Category, SubCategory, TxType


@pytest.mark.django_db
def test_reference_filters():
    tx1 = TxType.objects.create(name="Type1")
    tx2 = TxType.objects.create(name="Type2")
    cat1 = Category.objects.create(name="Cat1", tx_type=tx1)
    cat2 = Category.objects.create(name="Cat2", tx_type=tx2)
    SubCategory.objects.create(name="Sub1", category=cat1)
    sub2 = SubCategory.objects.create(name="Sub2", category=cat2)

    client = APIClient()

    response = client.get(reverse("category-list"), {"tx_type": tx1.id})
    assert response.status_code == 200
    assert [c["id"] for c in response.data["results"]] == [cat1.id]

    response = client.get(reverse("subcategory-list"), {"category": cat2.id})
    assert response.status_code == 200
    assert [s["id"] for s in response.data["results"]] == [sub2.id]
