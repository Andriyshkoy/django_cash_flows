from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from core.views import TransactionViewSet
from reference.views import (
    CategoryViewSet,
    StatusViewSet,
    SubCategoryViewSet,
    TxTypeViewSet,
)

router = DefaultRouter()
router.register(r"transactions", TransactionViewSet)
router.register(r"statuses", StatusViewSet)
router.register(r"types", TxTypeViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"sub-categories", SubCategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
