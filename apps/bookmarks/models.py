from django.db import models
from core.models import BaseModels


class SavedBookmarks(BaseModels):
    url = models.URLField()
    description = models.CharField(max_length=255)
    source = models.CharField(max_length=100)
