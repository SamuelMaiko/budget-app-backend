from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_wallet.serializers import WalletSerializer

class MyWalletsView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        user = request.user
        wallets = user.wallets.all()
        serializer = WalletSerializer(wallets, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)