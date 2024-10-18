from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_expense_items.serializers import ExpenseItemSerializer

class CreateExpenseItemsView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer=ExpenseItemSerializer(data=request.data, context={
            type:"just-create"
        })
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    