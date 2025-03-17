from rest_framework.permissions import BasePermission
from pixorin_dns.models import LicenseKey
from django.utils import timezone

class HasValidLicense(BasePermission):
    def has_permission(self, request, view):
        # بررسی کلید لایسنس معتبر (نیازی به user نیست)
        license_key = request.headers.get('Authorization', None)  # دریافت لایسنس از هدر
        if not license_key:
            return False

        # حذف "Bearer" از مقدار لایسنس در هدر
        if license_key.startswith("Bearer "):
            license_key = license_key[7:]

        try:
            # جستجو برای لایسنس با کلید وارد شده
            license = LicenseKey.objects.get(key=license_key, is_active=True)
            # بررسی تاریخ انقضا لایسنس
            if license.expiration_date < timezone.now():
                return False  # لایسنس منقضی شده
        except LicenseKey.DoesNotExist:
            return False  # لایسنس پیدا نشد

        return True  # اگر لایسنس معتبر باشد
