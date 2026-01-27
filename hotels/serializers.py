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
            'email',
            'telephone',
            'prix',
            'devise',
            'image',
            'image_url',
            'owner',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at', 'image_url']
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
            'email': {'required': False, 'allow_blank': True, 'allow_null': True},
            'telephone': {'required': False, 'allow_blank': True, 'allow_null': True},
            'description': {'required': False, 'allow_blank': True},
        }

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None