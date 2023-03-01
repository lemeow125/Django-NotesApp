from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(owner=user).order_by('date_created')
        return queryset
