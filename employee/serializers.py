from rest_framework import serializers
from django.utils import timezone
from .models import employee


class employeemodelserializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'
        read_only_field = ("created_at", "updated_at")

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.created_at = timezone.now()
        obj.save()
        return obj
