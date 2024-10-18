from django.db import models
from a_shared.models import BaseModel
from .Week import Week
from a_expense_items.models import ExpenseItem

class WeekItemAssociation(BaseModel):
    amount_allocated = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    amount_used = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    expense_item=models.ForeignKey(ExpenseItem, on_delete=models.CASCADE, related_name="week_item_association")
    week=models.ForeignKey(Week, on_delete=models.CASCADE, related_name="week_item_association")

    class Meta:
        db_table = "week_item_association"

    def __str__(self):
        return f"{self.week.user.username}'s association btn:  {self.week.name} - {self.expense_item.name}"
    
    @property
    def remaining_amount(self):
        return self.amount_allocated - self.amount_used