from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_weekly_budget.serializers import MyCustomItemSerializer
from a_weekly_budget.models import WeekItemAssociation
from a_wallet.models import Wallet
from django.db.models import F

class EditWeekItemView(APIView):
    permission_classes=[IsAuthenticated]

    def put(self, request, week_item_id):
        # name and amount_allocated 
        try:
            week_item_association = WeekItemAssociation.objects.get(id=week_item_id)
        except WeekItemAssociation.DoesNotExist as e:
            return Response({"error": "week-item not found."}, status=status.HTTP_404_NOT_FOUND)
        
        inc_amount_allocated=request.data.get('amount_allocated',None)
        if inc_amount_allocated is not None:
                weekly_wallet=Wallet.objects.filter(
                name="Weekly wallet", 
                user=request.user
                )
                # checking if there is enough money in the weekly wallet
                if weekly_wallet.first().balance+week_item_association.amount_allocated-inc_amount_allocated<=0:
                     return Response({"error": "Not enough balance in the wallet."}, status=status.HTTP_400_BAD_REQUEST)
                # update the amounts
                weekly_wallet.update(
                    balance=F('balance')+week_item_association.amount_allocated-inc_amount_allocated
                    ) 
                
        serializer=MyCustomItemSerializer(week_item_association, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    