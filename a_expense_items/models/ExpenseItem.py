from django.db import models
from a_shared.models import BaseModel
from django.conf import settings

class ExpenseItem(BaseModel):
    name = models.CharField(max_length=255)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="expense_items")

    class Meta:
        db_table = "expense_items"

    def __str__(self):
        return self.name
