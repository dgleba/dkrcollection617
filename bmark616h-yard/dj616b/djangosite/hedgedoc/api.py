from rest_framework import viewsets, permissions

from . import serializers
from . import models


class NotesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Notes class"""

    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesSerializer
    permission_classes = [permissions.IsAuthenticated]
