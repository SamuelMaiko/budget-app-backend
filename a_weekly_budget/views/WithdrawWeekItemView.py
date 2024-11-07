from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_weekly_budget.models import WeekItemAssociation
from a_weekly_budget.permissions import IsOwnerOfWeek
from a_weekly_budget.serializers import StatementSerializer

class WithdrawWeekItemView(APIView):
    permission_classes=[IsAuthenticated, IsOwnerOfWeek]

    def post(self, request, week_item_id):

        try:
            week_item = WeekItemAssociation.objects.get(id=week_item_id)
        except WeekItemAssociation.DoesNotExist:
            return Response({"error": "Week item not found"}, status=status.HTTP_404_NOT_FOUND)
        # checking if it belongs to the logged in user
        self.check_object_permissions(request,week_item.week)
        self.check_object_permissions(request,week_item.expense_item)

        # checking if the remaining amount is sufficient
        if week_item.remaining_amount<request.data.get('amount',0):
            return Response({"error": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)

        # recording the statement
        statement_data = {
        'amount': request.data.get('amount'),
        'description': f"({week_item.expense_item.name}) {request.data.get('description')}",
        'week':week_item.week.id,
        'item_involved':week_item.expense_item.id

            }
        
        serializer = StatementSerializer(data=statement_data)
        if serializer.is_valid():
            serializer.save(week=week_item.week, item_involved=week_item.expense_item)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"success": "Withdraw successful."}, status=status.HTTP_200_OK)