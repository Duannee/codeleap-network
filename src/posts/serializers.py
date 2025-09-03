from rest_framework import serializers
from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d/%m/%Y %H:%M:%S",
        read_only=True,
        )
    
    class Meta:
        model = Posts
        fields = [
            "id",
            "username",
            "created_at",
            "title",
            "content",
        ]
        read_only_fields = ["id"]


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["title", "content"]

    def validate(self, attrs):
        if "username" in getattr(self, "initial_data", {}):
            raise serializers.ValidationError({"username": "This field cannot be updated"})
        return attrs