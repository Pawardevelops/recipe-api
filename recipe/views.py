
from rest_framework import viewsets
from core.models import Recipe
from recipe import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    """view to manage recipe APIs."""
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for the request."""
        if self.action == 'list':
            return serializers.RecipeSerializer
        return serializers.RecipeDetailSerializer
    
    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)