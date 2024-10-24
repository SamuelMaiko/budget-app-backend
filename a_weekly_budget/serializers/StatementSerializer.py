from rest_framework import serializers
from a_weekly_budget.models import Statement

class StatementSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Statement
        fields = ['id', 'amount', 'description', 'week', 'item_involved', 'created_at', 'updated_at']
