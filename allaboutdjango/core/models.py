from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Devlog(models.Model):
    title = models.CharField(max_length=1024, unique=True)
    content = models.TextField()
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

class SiteVisit(models.Model):
    region = models.CharField(max_length=50, null=True, blank=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
