from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_wallet.models import Wallet
from a_wallet.permissions import IsOwnerOfWallet
from a_wallet.models import Transaction

class DepositFundsView(APIView):
    permission_classes=[IsAuthenticated, IsOwnerOfWallet]

    def post(self, request, wallet_id):
        inc_amount = request.data.get('amount')

        # Check if all required fields are present
        if not inc_amount:
            return Response({"error": "amount is required."}, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist as e:
            return Response({"error": "Wallet not found."}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, wallet)

        wallet.balance+=inc_amount
        wallet.save()

        # creating a transaction for the wallet 
        Transaction.objects.create(
            type='deposit',
            amount=inc_amount,
            wallet=wallet,
        )

            
        return Response({"success": "Deposit successful.","new_amount":wallet.balance}, status=status.HTTP_200_OK)