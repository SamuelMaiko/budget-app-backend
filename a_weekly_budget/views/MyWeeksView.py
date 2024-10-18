from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from a_weekly_budget.serializers import WeekSerializer

class MyWeeksView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        user = request.user
        weeks = user.weeks.all()
        serializer = WeekSerializer(weeks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)