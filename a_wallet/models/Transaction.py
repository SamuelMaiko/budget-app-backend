from django.db import models
from a_shared.models import BaseModel
from .Wallet import Wallet

class Transaction(BaseModel):
    TRANSACTION_TYPE_CHOICES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
        ('deposit', 'Deposit'),
    ]
    
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES, default="debit")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="",null=True, blank=True )
    wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")
    other_wallet=models.ForeignKey(Wallet, on_delete=models.SET_NULL, related_name="transactions_involved_in", null=True, blank=True)

    class Meta:
        db_table = "transactions"
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.get_type_display()} of {self.amount} involving {self.wallet.user.username}'s {self.wallet.name}  {f'and {self.other_wallet.user.username}'+" s" if self.other_wallet else "" } {self.other_wallet.name if self.other_wallet else " only"}"
