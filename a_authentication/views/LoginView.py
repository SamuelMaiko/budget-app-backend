from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[]

    def post(self, request):
        inc_username=request.data.get('username')
        inc_password=request.data.get('password')

        if not inc_password and not inc_password:
            return Response({"error":"username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        if not inc_username:
            return Response({"error":"username required"}, status=status.HTTP_400_BAD_REQUEST)

        if not inc_password:
            return Response({"error":"password required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user=authenticate(request, username=inc_username, password=inc_password)

        if user is not None:
            login(request, user)
            # jwt
            refresh = RefreshToken.for_user(user)

            response_dict={
                # "user":dict(username=user.username, email=user.email),
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }
            
            return Response(response_dict, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_404_NOT_FOUND)
        