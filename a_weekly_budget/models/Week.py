from django.db import models
from a_shared.models import BaseModel
from django.conf import settings
from a_expense_items.models import ExpenseItem

class Week(BaseModel):
    name = models.CharField(max_length=255, default="", blank=True, null=True, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    used_cash = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="weeks")
    expense_items=models.ManyToManyField(ExpenseItem, related_name="weeks", blank=True, through='WeekItemAssociation')

    class Meta:
        db_table = "weeks"

    def __str__(self):
        return f"{self.user.username}'s Week: {self.name} ({self.start_date} - {self.end_date})"

    @property
    def remaining_cash(self):
        return self.total_expenses - self.used_cash