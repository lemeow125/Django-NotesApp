from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    date_created = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'date_created', 'owner', 'public')
        read_only_fields = ('id', 'date_created', 'owner')
