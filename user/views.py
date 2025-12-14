"""Views for the user API."""

from rest_framework import generics
from rest_framework import authentication, permissions
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.contrib.auth import get_user_model

class CreateTokenView(ObtainAuthToken):
    """Create a new token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

     

class CreateUserView(generics.CreateAPIView):
    """Create a new user."""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Create and return a new user."""
        serializer.save()

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
    
    def perform_update(self, serializer):
        """Update and return the authenticated user."""
        serializer.save()
    