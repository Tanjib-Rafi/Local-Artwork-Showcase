from rest_framework import serializers
from .models import  Artist, Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ('title', 'description', 'creation_date', 'image_url')


#Serializer for artist profiles with related artworks
class ArtistProfileSerializer(serializers.ModelSerializer):
    artworks = ArtworkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('user', 'bio', 'artworks')
        