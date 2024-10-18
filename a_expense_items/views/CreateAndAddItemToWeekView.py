from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_expense_items.serializers import ExpenseItemSerializer
from a_weekly_budget.models import Week

class CreateAndAddItemToWeekView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        # name, amount, week_id
        inc_week_id=request.data.pop('week_id', None)
        if not inc_week_id:
            return Response({"error": "week_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            week = Week.objects.get(id=inc_week_id)
        except Week.DoesNotExist:
            return Response({"error": "Week not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=ExpenseItemSerializer(data=request.data, context={
            "type":"create-and-add-to-week",
            "week":week
        })
        if serializer.is_valid():
            serializer.save(user=request.user)

            response_dict=serializer.data.copy()
            response_dict["amount_allocated"]=request.data.get("amount")
            return Response(response_dict, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    