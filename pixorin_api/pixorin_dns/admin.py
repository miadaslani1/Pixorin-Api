from django.contrib import admin
from .models import LicenseKey, DNSRecord
import uuid
from django.utils.timezone import now, timedelta

# اکشن برای تمدید تاریخ انقضا
@admin.action(description="تمدید لایسنس (۳۰ روز اضافه کن)")
def extend_license(modeladmin, request, queryset):
    for license in queryset:
        license.expiration_date += timedelta(days=30)  # تمدید تاریخ انقضا
        license.save()
    modeladmin.message_user(request, f"{queryset.count()} لایسنس تمدید شد.")

# مدیریت LicenseKey در پنل ادمین
class LicenseKeyAdmin(admin.ModelAdmin):
    list_display = ("key", "user", "is_active", "expiration_date","name","status_icon")  # استفاده از `expiration_date`
    list_filter = ("is_active", "expiration_date")  # استفاده از `expiration_date`
    search_fields = ("key", "user__username")
    actions = [extend_license]  # دکمه "تمدید لایسنس"
    def status_icon(self, obj):
        if obj.is_active:
            return "✔️"
        else:
            return "❌"
    status_icon.short_description = 'Status'

# مدیریت DNSRecord در پنل ادمین
class DNSRecordAdmin(admin.ModelAdmin):
    list_display = ("name", "primary_dns", "secondary_dns", "created_at")  # استفاده از `created_at`
    list_filter = ("created_at",)  # استفاده از `created_at`
    search_fields = ("name", "primary_dns", "secondary_dns")

# ثبت مدل‌ها در ادمین
admin.site.register(LicenseKey, LicenseKeyAdmin)
admin.site.register(DNSRecord, DNSRecordAdmin)
