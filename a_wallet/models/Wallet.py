from django.db import models
from a_shared.models import BaseModel
from django.conf import settings

class Wallet(BaseModel):
    COLOR_CHOICES = [
        ('#1E90FF', 'Ocean Blue'),
        ('#3EB489', 'Mint Green'),
        ('#FF4500', 'Sunset Orange'),
        ('#9370DB', 'Lavender Purple'),
        ('#FFD700', 'Golden Yellow'),
        ('#36454F', 'Charcoal Gray'),
        ('#FFB6C1', 'Soft Pink'),
        ('#228B22', 'Forest Green'),
    ]

    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    color_theme = models.CharField(max_length=50, choices=COLOR_CHOICES, default='#1E90FF') 
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wallets")

    class Meta:
        db_table = "wallets"

    def __str__(self):
        return f"{self.user.username}'s {self.name} Wallet"