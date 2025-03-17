import random
import string  
from datetime import timedelta
from django.utils import timezone
from rest_framework import viewsets
from pixorin_dns.models import LicenseKey
from .serializers import *
from rest_framework.response import Response
from .permissions import HasValidLicense

class DNSViewSet(viewsets.ModelViewSet):
    queryset = DNSRecord.objects.all()
    serializer_class = DNSRecordSerializer
    permission_classes = [HasValidLicense]  

   
class LicenseKeyViewSet(viewsets.ModelViewSet):
    queryset = LicenseKey.objects.all()
    serializer_class = LicenseKeySerializer
    permission_classes = [HasValidLicense]  

    def generate_license_key(self):
        # تولید کلید لایسنس تصادفی
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

    def create(self, request, *args, **kwargs):
        # تولید کلید لایسنس جدید برای کاربر
        expiration_date = timezone.now() + timedelta(days=30)  # مدت زمان اشتراک 30 روز
        key = self.generate_license_key()
        license_key = LicenseKey.objects.create(user=request.user, key=key, expiration_date=expiration_date)
        serializer = self.get_serializer(license_key)
        return Response(serializer.data)
    
    
    def list(self, request, *args, **kwargs):
        for license in LicenseKey.objects.all():
            if license.expiration_date < timezone.now() and license.is_active:
                license.is_active = False
                license.save()
        return super().list(request, *args, **kwargs)        