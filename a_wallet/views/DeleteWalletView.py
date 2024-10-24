from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_wallet.models import Wallet
from a_wallet.permissions import IsOwnerOfWallet


class DeleteWalletView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOfWallet]

    def delete(self, request, wallet_id):
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)
        # checking if it belongs to the logged in user
        self.check_object_permissions(request,wallet)

        if wallet.name =="Weekly wallet":
            return Response({"error": "Not allowed to delete weekly wallet."}, status=status.HTTP_403_FORBIDDEN)

        wallet.delete()
        return Response({"success": "Wallet deleted successfully."}, status=status.HTTP_204_NO_CONTENT)