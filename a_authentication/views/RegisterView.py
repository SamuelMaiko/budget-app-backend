from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from a_authentication.models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class RegisterView(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[]

    def post(self, request):
        inc_username=request.data.get('username')
        inc_email=request.data.get('email')
        inc_password=request.data.get('password')

        if not inc_password and not inc_password and not inc_username:
            return Response({"error":"username, email and password required"}, status=status.HTTP_400_BAD_REQUEST)

        if not inc_username:
            return Response({"error":"username required"}, status=status.HTTP_400_BAD_REQUEST)

        if not inc_email:
            return Response({"error":"username required"}, status=status.HTTP_400_BAD_REQUEST)

        if not inc_password:
            return Response({"error":"password required"}, status=status.HTTP_400_BAD_REQUEST)
        

        # Validate email format
        try:
            validate_email(inc_email)  # Validates the email format
        except ValidationError:
            return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)

  
        # Check for existing username
        if CustomUser.objects.filter(username=inc_username).exists():
            return Response({'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)

        # Check for existing email
        if CustomUser.objects.filter(email=inc_email).exists():
            return Response({'error': 'Email is already registered'}, status=status.HTTP_400_BAD_REQUEST)

        # Create user
        user = CustomUser.objects.create_user(username=inc_username, email=inc_email, password=inc_password)

        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)