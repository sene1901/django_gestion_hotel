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
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None