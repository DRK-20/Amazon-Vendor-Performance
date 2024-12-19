from django.db import models
from django.contrib.auth.models import User

class RegisteredProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_products')
    asin = models.CharField(max_length=20, unique=True)
    product_name = models.CharField(max_length=255)
    average_rating = models.CharField(max_length=10, null=True, blank=True)
    rating_breakdown = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} ({self.asin})"
