from rest_framework import serializers
from a_wallet.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    type=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'type', 'amount', 'description', 'wallet', 'other_wallet','created_at', 'updated_at']
        extra_kwargs ={
            'description':{'required':False}
        }

    def get_type(self, obj):
        wallet = self.context.get("wallet")
        return "Credit" if obj.other_wallet == wallet else "Deposit" if obj.type == "deposit" else "Debit"


    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value
    
    def to_representation(self, instance):
        """Customize the serialized output."""
        representation = super().to_representation(instance)
        representation['wallet'] = {
            'id': instance.wallet.id,
            'name': instance.wallet.name, 
        }
        representation['other_wallet'] = {
            'id': instance.other_wallet.id if instance.other_wallet else None,
            'name': instance.other_wallet.name if instance.other_wallet else None,  
        }
        return representation