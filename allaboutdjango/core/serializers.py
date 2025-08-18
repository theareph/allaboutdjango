from rest_framework import serializers

from .models import Devlog, Book


class DevlogSerializer(serializers.ModelSerializer):
    published_by = serializers.SerializerMethodField()

    class Meta:
        model = Devlog
        fields = ["title", "content", "inserted_at", "updated_at", "published_by"]

    def get_published_by(self, obj):
        return obj.published_by.username if obj.published_by else None

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["isbn", "name", "author"]