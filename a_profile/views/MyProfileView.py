from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from a_profile.models import Profile
from a_profile.serializers import ProfileSerializer
from rest_framework import status

class MyProfileView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)