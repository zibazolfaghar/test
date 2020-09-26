from rest_framework import serializers
from .models import book


class bookserializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    Author = serializers.CharField(max_length=150)
    store_name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    image = serializers.ImageField(default='',use_url=True)
    fav = serializers.BooleanField(default=False)

class bookmodelserializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'
