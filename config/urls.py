from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    TransactionCreateView,
    TransactionDeleteView,
    TransactionListView,
    TransactionUpdateView,
    TransactionViewSet,
)
from reference.views import (
    CategoryViewSet,
    StatusViewSet,
    SubCategoryViewSet,
    TxTypeViewSet,
)
from users.views import SignUpView

router = DefaultRouter()
router.register(r"transactions", TransactionViewSet, basename="transaction")
router.register(r"statuses", StatusViewSet)
router.register(r"types", TxTypeViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"sub-categories", SubCategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/register/", SignUpView.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TransactionListView.as_view(), name="transactions"),
    path("transactions/add/", TransactionCreateView.as_view(), name="transaction-add"),
    path(
        "transactions/<int:pk>/edit/",
        TransactionUpdateView.as_view(),
        name="transaction-edit",
    ),
    path(
        "transactions/<int:pk>/delete/",
        TransactionDeleteView.as_view(),
        name="transaction-delete",
    ),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
