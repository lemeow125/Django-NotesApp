from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import Note


class CustomUserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(
        many=True, allow_null=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'notes']
        read_only_fields = ['id', 'notes']
