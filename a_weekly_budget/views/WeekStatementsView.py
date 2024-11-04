from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_weekly_budget.permissions import IsOwnerOfWeek
from a_weekly_budget.models import Week, Statement
from a_weekly_budget.serializers import StatementSerializer
from django.db.models import Q


class WeekStatementsView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOfWeek]

    def get(self, request, week_id):
        try:
            week = Week.objects.get(id=week_id)
        except Week.DoesNotExist:
            return Response({"error": "Week not found"}, status=status.HTTP_404_NOT_FOUND)
        # checking if it belongs to the logged in user
        self.check_object_permissions(request,week)
        
        statements=Statement.objects.filter(week=week)
        serializer=StatementSerializer(statements, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)