from rest_framework import serializers
from a_wallet.models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model=Wallet
        fields=['id', 'name', 'balance', 'color_theme','created_at','updated_at']

    def __init__(self, *args, **kwargs):
        super(WalletSerializer, self).__init__(*args, **kwargs)
        # If it's an update (instance exists), make 'name' not required
        if self.instance:
            self.fields['name'].required = False

    def validate_balance(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value