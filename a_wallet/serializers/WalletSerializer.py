from rest_framework import serializers
from a_wallet.models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model=Wallet
        fields=['id', 'name', 'balance', 'color_theme','created_at','updated_at']

    def validate_balance(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value