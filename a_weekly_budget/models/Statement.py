from django.db import models
from a_shared.models import BaseModel
from .Week import Week
from a_expense_items.models import ExpenseItem

class Statement(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="", null=True, blank=True)
    week=models.ForeignKey(Week, on_delete=models.CASCADE, related_name="statements")
    item_involved=models.ForeignKey(ExpenseItem, on_delete=models.SET_NULL, related_name="statements_involved_in", null=True)

    class Meta:
        db_table = "statements"
        ordering=('-created_at',)

    def __str__(self):
        return f"{self.week.user.username} s Statement:  {self.amount} - {self.description[:30] if self.description else ''}"
