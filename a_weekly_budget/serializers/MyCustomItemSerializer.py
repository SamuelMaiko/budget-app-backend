from rest_framework import serializers
from a_weekly_budget.models import WeekItemAssociation
from a_wallet.models import Wallet
from decimal import Decimal

class MyCustomItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='expense_item.name', required=False)
    remaining_amount = serializers.SerializerMethodField()
    amount_allocated = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    # amount_allocatd = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = WeekItemAssociation
        fields = ['id', 'name','amount_allocated', 'amount_used', 'remaining_amount',]

    def get_remaining_amount(self, obj):
        return obj.remaining_amount 
    # def get_amount_allocatd(self, obj):
    #     if obj.expense_item.name!="Other":
    #         return obj.amount_allocated 
    #     else:
    #         wallet=Wallet.objects.get(name="Weekly wallet", user=obj.expense_item.user)
    #         obj.amount_allocated=(wallet.balance+obj.week.used_cash) - obj.week.total_expenses
    #         obj.save()
    #         return Decimal(obj.amount_allocated)
    
    def update(self, instance, validated_data):
        expense_item=validated_data.pop('expense_item', None)

        instance.amount_allocated = validated_data.get('amount_allocated', instance.amount_allocated)
        instance.expense_item.name = validated_data.get("name", instance.expense_item.name)

        

        if instance.amount_allocated < instance.amount_used:
            raise serializers.ValidationError("Allocated amount cannot be less than used amount.")
        
        instance.save()
        instance.expense_item.save()
        return instance