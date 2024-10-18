from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_weekly_budget.serializers import WeekSerializer, MyCustomItemSerializer
from a_weekly_budget.models import Week, WeekItemAssociation
from a_weekly_budget.permissions import IsOwnerOfWeek

class WeekDetailView(APIView):
    permission_classes=[IsAuthenticated, IsOwnerOfWeek]

    def get(self, request, week_id):
        try:
            week = Week.objects.get(id=week_id)
        except Week.DoesNotExist:
            return Response({"error": "Week not found"}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, week)
        
        serializer = WeekSerializer(week)
        response_data=serializer.data.copy()

        # getting the week's expense items
        sort_of_items=WeekItemAssociation.objects.filter(week=week).all()
        serializer_two=MyCustomItemSerializer(sort_of_items, many=True)

        response_data["expense_items"]=serializer_two.data

        return Response(response_data, status=status.HTTP_200_OK)