from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        "created_at": ["gte", "lte"],
        "status": ["exact"],
        "tx_type": ["exact"],
        "category": ["exact"],
        "sub_category": ["exact"],
    }

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "core/transaction_list.html"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = [
        "status",
        "tx_type",
        "category",
        "sub_category",
        "amount",
        "comment",
    ]
    template_name = "core/transaction_form.html"
    success_url = reverse_lazy("transactions")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = [
        "status",
        "tx_type",
        "category",
        "sub_category",
        "amount",
        "comment",
    ]
    template_name = "core/transaction_form.html"
    success_url = reverse_lazy("transactions")

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = "core/transaction_confirm_delete.html"
    success_url = reverse_lazy("transactions")

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
