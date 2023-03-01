from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import Note


class CustomUserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'notes']
