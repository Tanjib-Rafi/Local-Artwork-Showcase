from .models import Artist, Artwork
from .serializers import UserRegistrationSerializer,ArtistProfileSerializer, ArtworkSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


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
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            access_token = request.headers.get('Authorization').split(' ')[1]
            token = AccessToken(access_token)
            token.blacklist()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


#only authenticated user can view his/her profile
class ArtistProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ArtistProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return self.request.user.artist_profile
        except Artist.DoesNotExist:
            return None
    
#artwork create and list api
class ArtworkListCreateView(generics.ListCreateAPIView):
    serializer_class = ArtworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Artwork.objects.filter(artist__user=self.request.user)

    def perform_create(self, serializer):
        artist_profile = self.request.user.artist_profile
        serializer.save(artist=artist_profile)

#delete and update artwork for authenticated user
class ArtworkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Artwork.objects.filter(artist__user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj