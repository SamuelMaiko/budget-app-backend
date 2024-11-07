from rest_framework import serializers
from a_weekly_budget.models import Statement

class StatementSerializer(serializers.ModelSerializer):
    item_involved=serializers.SerializerMethodField()
        
    class Meta:
        model = Statement
        fields = ['id', 'amount', 'description', 'week', 'item_involved', 'created_at', 'updated_at']
    
    def get_item_involved(self, obj):
        return obj.item_involved.name
