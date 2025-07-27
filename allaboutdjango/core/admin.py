from django.contrib import admin
from .models import Devlog

# Register your models here.

@admin.register(Devlog)
class DevlogAdmin(admin.ModelAdmin):
    raw_id_fields = ["published_by",]
    list_display = ["title", "published_by", "inserted_at", "updated_at"]