from rest_framework import serializers
from a_expense_items.models import ExpenseItem
from a_weekly_budget.models import WeekItemAssociation


class ExpenseItemSerializer(serializers.ModelSerializer):
    in_work=serializers.SerializerMethodField()

    class Meta:
        model = ExpenseItem
        fields = ['id', 'name','in_work']

    def get_in_work(self, obj):
        week=self.context.get('week', None)
        if week is not None:
            return WeekItemAssociation.objects.filter(week=week, expense_item=obj).exists()
        return False
# class ExpenseItemSerializer(serializers.ModelSerializer):
#     amount = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True, required=False)

#     class Meta:
#         model = ExpenseItem
#         fields = ['id', 'name', 'amount']

#     def create(self, validated_data):
#         types=self.context.get("type")
#         if types=="just-create":
#             expense_item = ExpenseItem.objects.create(**validated_data)

#         else:
#             amount = validated_data.pop('amount', None)
#             week=self.context.get("week")
#             # create expense item with just the name
#             expense_item = ExpenseItem.objects.create(**validated_data)
#             WeekItemAssociation.objects.create(week=week, expense_item=expense_item,amount_allocated=amount)

#         return expense_item