from django.contrib.auth.models import User
from django.db import models

class order(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField()