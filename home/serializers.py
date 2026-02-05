from rest_framework import serializers
from .models import SystemStatus

class SystemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemStatus
        fields = "__all__"
