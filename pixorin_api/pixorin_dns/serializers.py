from rest_framework import serializers
from .models import *


class DNSRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNSRecord
        fields = ['name', 'primary_dns', 'secondary_dns']

class LicenseKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseKey
        fields = ['key', 'expiration_date', 'is_active']