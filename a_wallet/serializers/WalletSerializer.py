from rest_framework import serializers
from a_wallet.models import Wallet
from rest_framework.exceptions import ValidationError

class WalletSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model=Wallet
        fields=['id', 'name', 'balance', 'color_theme','created_at','updated_at']

    def update(self, instance, validated_data):
         # Check if the user is trying to change the name of the "Weekly wallet"
        if instance.name == "Weekly wallet" and 'name' in validated_data:
            raise ValidationError({"error": "Not allowed to edit the name of the Weekly wallet."})

        instance.balance=validated_data.get('balance', instance.balance)
        instance.color_theme=validated_data.get('color_theme', instance.color_theme)
        instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        super(WalletSerializer, self).__init__(*args, **kwargs)
        # If it's an update (instance exists), make 'name' not required
        if self.instance:
            self.fields['name'].required = False

    def validate_balance(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value