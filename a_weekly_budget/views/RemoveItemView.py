from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_weekly_budget.serializers import WeekSerializer
from a_weekly_budget.models import Week, WeekItemAssociation
from a_expense_items.models import ExpenseItem
from a_weekly_budget.permissions import IsOwnerOfWeek
from a_wallet.models import Transaction, Wallet
from django.db.models import F

class RemoveItemView(APIView):
    permission_classes=[IsAuthenticated, IsOwnerOfWeek]

    def delete(self, request, week_id):
        inc_item_id=request.data.get('item_id')

        if not inc_item_id:
            return Response({"error": "item_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            week = Week.objects.get(id=week_id)
        except Week.DoesNotExist as e:
            return Response({"error": "Week not found."}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            expense_item = ExpenseItem.objects.get(id=inc_item_id)
        except ExpenseItem.DoesNotExist as e:
            return Response({"error": "Expense item not found."}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, week)
        # I know the permission is for the week but it can work also for items
        self.check_object_permissions(request, expense_item)

        association_set=WeekItemAssociation.objects.filter(expense_item=expense_item, week=week)
        if association_set.exists():
            association=association_set.first()
            # transfer the remaining money to wallet 
            remaining_money=association.remaining_amount
            wallet=Wallet.objects.filter(
            name="Weekly wallet", 
            user=association.week.user
            ).update(
                balance=F('balance')+remaining_money
                )
            print(wallet)
            Transaction.objects.create(
                type="credit",
                amount=remaining_money,
                wallet_id=wallet,
                description=f"item ({expense_item.name}) removed from week ({week.name}). remaining money -> ({remaining_money})"
                )
            
            association.delete()
            return Response({"success": "Item removed successfully."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Item not found in week."}, status=status.HTTP_404_NOT_FOUND)
        


    