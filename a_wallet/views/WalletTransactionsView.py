from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_wallet.models import Wallet
from a_wallet.permissions import IsOwnerOfWallet
from a_wallet.serializers import TransactionSerializer
from a_wallet.models import Transaction
from django.db.models import Q


class WalletTransactionsView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOfWallet]

    def get(self, request, wallet_id):
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)
        # checking if it belongs to the logged in user
        self.check_object_permissions(request,wallet)
        
        transactions=Transaction.objects.filter(
            Q(wallet=wallet) | Q(other_wallet=wallet)
        )
        serializer=TransactionSerializer(transactions, many=True, context={"wallet":wallet})
        
        return Response(serializer.data, status=status.HTTP_200_OK)