from rest_framework import serializers
from .models import User
from artworks.models import Artist

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('email', 'user_name', 'password', 'bio')

    def validate_email(self, value):
        # Check email is in a valid format
        if '@' not in value:
            raise serializers.ValidationError("Invalid email format")
        return value

    def validate_user_name(self, value):
        # Check username is at least 5 characters long
        if len(value) < 5:
            raise serializers.ValidationError("Username must be at least 5 characters long")
        return value

#if user not provide bio in registration "Artist bio" will be their default bio
    def create(self, validated_data):
        bio = validated_data.pop('bio', 'Artist bio')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        Artist.objects.create(user=user, bio=bio)
        return user
