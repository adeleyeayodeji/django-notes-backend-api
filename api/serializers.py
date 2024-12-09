from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    # Meta class is used to define metadata for the serializer
    # model is the model that the serializer is based on
    # fields is the fields that are included in the serialized output
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    # create method is used to create a new user
    # validated_data is the data that is passed to the serializer
    # username, email, and password are the fields that are passed to the serializer
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "author", "created_at", "updated_at"]
        # author is a field that is read-only
        extra_kwargs = {"author": {"read_only": True}}
