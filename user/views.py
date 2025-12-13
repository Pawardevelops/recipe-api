"""Views for the user API."""

from rest_framework import generics
from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user."""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Create and return a new user."""
        serializer.save()