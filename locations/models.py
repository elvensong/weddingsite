from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models. CharField(max_length=50)
    country = models.CharField(max_length=50)
    map_link = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
