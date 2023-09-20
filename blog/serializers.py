from rest_framework import serializers

from .models import BlogPage


class BlogPageListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = BlogPage
        fields = ("id", "title", "slug", "author", "date", "body", "image")

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.file.url) if obj.image else None


class BlogPageDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = BlogPage
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.file.url) if obj.image else None
