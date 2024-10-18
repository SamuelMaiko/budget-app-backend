from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_weekly_budget.serializers import WeekSerializer, MyCustomItemSerializer
from a_weekly_budget.models import WeekItemAssociation

class EditWeekItemView(APIView):
    permission_classes=[IsAuthenticated]

    def put(self, request, week_item_id):
        # name and amount_allocated 
        try:
            work_item_association = WeekItemAssociation.objects.get(id=week_item_id)
        except WeekItemAssociation.DoesNotExist as e:
            return Response({"error": "week-item not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=MyCustomItemSerializer(work_item_association, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    