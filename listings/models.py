from django.db import models
from django.conf import settings
from django import forms

class Property(models.Model):
    """blank set to true makes the corresponding form fields not required"""

    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    CATEGORIES = {
        "Boys only": "boys only",
        "Girls only": "girls only",
        "Both": "both",
    }
    
    type = models.CharField(max_length=20,choices=CATEGORIES, null=True, blank=True)
    
    rent_per_month = models.CharField(max_length=7, null=True,blank=True)

    contact_1 = models.CharField(max_length=10)
    contact_2 = models.CharField(max_length=10, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 