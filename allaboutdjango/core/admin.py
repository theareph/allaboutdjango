from django.contrib import admin

from .models import Devlog, SiteVisit

# Register your models here.


@admin.register(Devlog)
class DevlogAdmin(admin.ModelAdmin):
    raw_id_fields = [
        "published_by",
    ]
    list_display = ["title", "published_by", "inserted_at", "updated_at"]


@admin.register(SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
    readonly_fields = ["inserted_at", "region"]
    list_display = ["inserted_at", "region"]
