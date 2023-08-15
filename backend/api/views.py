from django.conf import settings
from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from recipes.models import Ingredient, Tag, User, Recipe
from rest_framework import filters, permissions, serializers, status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.pagination import PageNumberPagination

from .serializers import (IngredientSerializer, RecipeReadSerializer,
                          RecipeWriteSerializer, TagSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с пользователями"""
    http_method_names = ['get', 'post', 'head']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_permissions(self):
        """Дает доступ к эндпоинту me только
            аутентифицированному пользователю"""
        if self.action == 'me':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с тегами."""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = None


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с ингредиентами."""
    # http_method_names = ['get']
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)


class RecipeViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с рецептами."""
    queryset = (
        Recipe.objects.select_related('author')
        .prefetch_related('ingredients', 'tags').all()
    )

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeReadSerializer
        return RecipeWriteSerializer