import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse
from rest_framework.test import APIClient

from reference.models import Category, Status, SubCategory, TxType

from .models import Transaction


@pytest.fixture
def data(db):
    user_model = get_user_model()
    user = user_model.objects.create_user(username="user", password="password")
    status = Status.objects.create(name="Бизнес")
    tx_type = TxType.objects.create(name="Списание")
    category = Category.objects.create(name="Маркетинг", tx_type=tx_type)
    sub_category = SubCategory.objects.create(name="Avito", category=category)
    return {
        "user": user,
        "status": status,
        "tx_type": tx_type,
        "category": category,
        "sub_category": sub_category,
    }


def test_transaction_validation(data):
    wrong_category = Category.objects.create(
        name="Инфраструктура", tx_type=data["tx_type"]
    )
    with pytest.raises(ValidationError):
        Transaction.objects.create(
            user=data["user"],
            status=data["status"],
            tx_type=data["tx_type"],
            category=wrong_category,
            sub_category=data["sub_category"],
            amount=1000,
        )


def test_transaction_api_create_and_filter(data):
    client = APIClient()
    token_response = client.post(
        reverse("token_obtain_pair"),
        {"username": "user", "password": "password"},
        format="json",
    )
    access = token_response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    response = client.post(
        reverse("transaction-list"),
        {
            "status": data["status"].id,
            "tx_type": data["tx_type"].id,
            "category": data["category"].id,
            "sub_category": data["sub_category"].id,
            "amount": "1000.00",
            "comment": "test",
        },
        format="json",
    )
    assert response.status_code == 201
    response = client.get(reverse("transaction-list"), {"tx_type": data["tx_type"].id})
    assert response.status_code == 200
    assert response.data["count"] == 1


def test_transaction_list_pagination(client, data):
    user = data["user"]
    client.force_login(user)
    for i in range(11):
        Transaction.objects.create(
            user=user,
            status=data["status"],
            tx_type=data["tx_type"],
            category=data["category"],
            sub_category=data["sub_category"],
            amount=1000 + i,
        )
    response = client.get(reverse("transactions"))
    assert response.status_code == 200
    assert len(response.context["object_list"]) == 10
    response = client.get(reverse("transactions"), {"page": 2})
    assert len(response.context["object_list"]) == 1
