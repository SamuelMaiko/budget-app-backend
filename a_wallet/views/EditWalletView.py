from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_wallet.models import Wallet
from a_wallet.serializers import WalletSerializer
from a_wallet.permissions import IsOwnerOfWallet

class EditWalletView(APIView):
    permission_classes=[IsAuthenticated, IsOwnerOfWallet]

    def put(self, request, wallet_id):
        # name and amount_allocated 
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)

        # checking if it belongs to the logged in user
        self.check_object_permissions(request,wallet)

        serializer=WalletSerializer(wallet, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    