
from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Hotel
        fields = [
            "id",
            "name",
            "description",
            "email",
            "telephone",
            "prix",
            "devise",
            "image",
            "image_url",
            "owner",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["owner", "created_at", "updated_at"]

    def get_image_url(self, obj):
        """
        Sécurisé pour Cloudinary (évite les 500 en prod)
        """
        try:
            if obj.image and hasattr(obj.image, "url"):
                return obj.image.url
        except Exception:
            return None
        return None
