from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from accounts.models import User


#Model for artist with user profile(one to one with User model)
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist_profile')
    bio = models.TextField()

    def __str__(self):
        return self.user.user_name

#Model for artwork with an artist(many to one with Artist model)
class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField()
    image_url = models.URLField()

    def __str__(self):
        return self.title
