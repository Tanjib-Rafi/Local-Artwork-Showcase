from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



#registration view
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#login view
class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            access_token = response.data.get('access', None)
            refresh_token = response.data.get('refresh', None)
            if access_token:
                user_id = self.decode_user_id_from_token(access_token)
                if user_id:
                    return Response({
                        'access': access_token,
                        'refresh': refresh_token,
                        'user_id': user_id,
                    })
        return response
    
    #excluding user_id from token
    def decode_user_id_from_token(self, token):
        try:
            access_token = AccessToken(token)
            return access_token.payload.get('user_id', None)
        except Exception as e:
            return None
        

#logout api and make the token blacklisted    
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            print(refresh_token)
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            raise e


