from django.db import models
from registrations.models import RegisteredProduct

class Analysis(models.Model):
    product = models.ForeignKey(RegisteredProduct, on_delete=models.CASCADE, related_name='analyses')
    issues = models.JSONField()
    suggestions = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.product.product_name}"
