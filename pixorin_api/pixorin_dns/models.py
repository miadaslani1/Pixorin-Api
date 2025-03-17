from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class DNSRecord(models.Model):
    name = models.CharField(max_length=255)  # مثلاً سرویس الکترو
    primary_dns = models.GenericIPAddressField()  # اصلی
    secondary_dns = models.GenericIPAddressField()  # ثانویه
    created_at = models.DateTimeField(auto_now_add=True,null=True)  

    def __str__(self):
        return self.name
    

class LicenseKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    expiration_date = models.DateTimeField()  # تاریخ انقضا
    is_active = models.BooleanField()  # وضعیت فعال بودن لایسنس
    name = models.CharField(max_length=30,null=True)

    def is_expired(self):
        return timezone.now() > self.expiration_date
    
    def save(self, *args, **kwargs):
        if self.expiration_date < timezone.now():
            self.is_active = False
        super(LicenseKey, self).save(*args, **kwargs) 


    def __str__(self):
        return str(self.key)  

