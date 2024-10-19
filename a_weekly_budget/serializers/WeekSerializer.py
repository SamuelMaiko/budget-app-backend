from rest_framework import serializers
from a_weekly_budget.models import Week

class WeekSerializer(serializers.ModelSerializer):
    # expense_items = ExpenseItemSerializer(many=True, required=False)
    remaining_cash=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Week
        fields = ['id', 'name', 'start_date', 'end_date', 'total_expenses','used_cash', 'remaining_cash']

    def get_remaining_cash(self, obj):
        return obj.remaining_cash