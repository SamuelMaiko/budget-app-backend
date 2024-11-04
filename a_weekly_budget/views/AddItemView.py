from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_weekly_budget.serializers import WeekSerializer
from a_weekly_budget.models import Week, WeekItemAssociation
from a_expense_items.models import ExpenseItem
from a_weekly_budget.permissions import IsOwnerOfWeek

class AddItemView(APIView):
    permission_classes=[IsAuthenticated, IsOwnerOfWeek]

    def post(self, request, week_id):
        inc_item_id=request.data.get('item_id')
        inc_amount=request.data.get('amount')

        if not inc_item_id:
            return Response({"error": "item_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        elif not inc_amount:
            return Response({"error": "amount is required."}, status=status.HTTP_400_BAD_REQUEST)
        
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

        if week.expense_items.filter(id=inc_item_id).exists():
            return Response({"error": "Expense item already added to this week."}, status=status.HTTP_400_BAD_REQUEST)

        association=WeekItemAssociation.objects.create(expense_item=expense_item, week=week, amount_allocated=inc_amount)
        # week.expense_items.add(expense_item)

        return Response({"id":association.id,"success":"Expense item added successfully."}, status=status.HTTP_200_OK)


    