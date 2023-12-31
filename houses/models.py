from django.db import models


class House(models.Model):
    """Model definition for Houses"""
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    address = models.CharField(max_length=140)
