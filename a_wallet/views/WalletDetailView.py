from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_wallet.serializers import WalletSerializer
from a_wallet.models import Wallet
from a_wallet.permissions import IsOwnerOfWallet

class WalletDetailView(APIView):
    permission_classes=[IsAuthenticated, IsOwnerOfWallet]

    def get(self, request, wallet_id):
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, wallet)
        
        serializer = WalletSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)