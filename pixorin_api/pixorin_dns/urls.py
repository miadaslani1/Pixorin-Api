from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DNSViewSet, LicenseKeyViewSet

router = DefaultRouter()
router.register(r'dns', DNSViewSet)
router.register(r'license-keys', LicenseKeyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]