from .models import Try1
from rest_framework import serializers

class TrySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Try1
        fields = '__all__'