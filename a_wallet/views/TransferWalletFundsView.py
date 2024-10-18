from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_wallet.models import Wallet
from a_wallet.permissions import IsOwnerOfWallet
from a_wallet.serializers import TransactionSerializer

class TransferWalletFundsView(APIView):
    permission_classes=[IsAuthenticated, IsOwnerOfWallet]

    def post(self, request):
        inc_from_wallet_id = request.data.get('from_wallet_id')
        inc_to_wallet_id = request.data.get('to_wallet_id')
        inc_amount = request.data.get('amount')
        inc_description = request.data.get('description', "")


        # Check if all required fields are present
        if not inc_from_wallet_id:
            return Response({"error": "from_wallet_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not inc_to_wallet_id:
            return Response({"error": "to_wallet_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not inc_amount:
            return Response({"error": "amount is required."}, status=status.HTTP_400_BAD_REQUEST)

        # transfer logic
        try:
            from_wallet = Wallet.objects.get(id=inc_from_wallet_id)
            to_wallet = Wallet.objects.get(id=inc_to_wallet_id)
        except Wallet.DoesNotExist as e:
            print(str(e))
            wallet_type = 'from_wallet' if 'from_wallet' in str(e) else 'to_wallet'
            return Response({"error": f"{wallet_type} not found."}, status=status.HTTP_404_NOT_FOUND)
            
        # checking if the wallets belong to the logged in user
        self.check_object_permissions(request, from_wallet)
        self.check_object_permissions(request, to_wallet)
        
        if from_wallet.balance < inc_amount:
            return Response({"error": "Insufficient funds."}, status=status.HTTP_400_BAD_REQUEST)
        
        from_wallet.balance -= inc_amount
        to_wallet.balance += inc_amount


        from_wallet.save()
        to_wallet.save()

        # recording the transaction
        transaction_data = {
        'type': 'debit',
        'amount': inc_amount,
        'description': inc_description,
        'wallet': from_wallet.id,
        'other_wallet': to_wallet.id
            }
        
        serializer = TransactionSerializer(data=transaction_data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"success": "Transfer completed."}, status=status.HTTP_200_OK)