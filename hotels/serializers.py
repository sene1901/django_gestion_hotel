from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Hotel
        fields = [
            'id',
            'name',
            'description',
            'prix',
            'image',
            'image_url',
            'owner',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
