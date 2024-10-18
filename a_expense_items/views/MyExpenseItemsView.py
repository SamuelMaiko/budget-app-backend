from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_expense_items.serializers import ExpenseItemSerializer
from a_weekly_budget.models import Week

class MyExpenseItemsView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        inc_week_id = request.GET.get('week_id', None)

        if inc_week_id:
            try:
                week = Week.objects.get(id=inc_week_id)
            except Week.DoesNotExist:
                return Response({"error": "Week not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            week = None

        user = request.user
        expense_items = user.expense_items.all()
        serializer = ExpenseItemSerializer(expense_items, many=True, context={"week": week})

        return Response(serializer.data, status=status.HTTP_200_OK)