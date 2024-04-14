from .models import Artist, Artwork
from .serializers import ArtistProfileSerializer, ArtworkSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated




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