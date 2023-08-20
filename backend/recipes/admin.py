from django.contrib import admin

from users.models import Follow

from recipes.models import (Favourites, Ingredient, IngredientAmount, Recipe,
                            ShoppingCart, Tag)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('amount', 'recipe', 'ingredient')
    search_fields = ('recipe__name', 'ingredient__name')


class IngredientInline(admin.TabularInline):
    model = IngredientAmount
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'in_favourite_count')
    search_fields = ('name', 'author__username', 'tags__name')
    list_filter = ('name', 'author__username', 'tags__name')
    readonly_fields = ('in_favourite_count', )
    inlines = (IngredientInline,)

    def in_favourite_count(self, recipe):
        """Подсчитывает сколько раз рецепт добавлен в избранное."""
        return recipe.favourite.count()

    in_favourite_count.short_description = 'В избранном'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user__username', 'following__username')


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'recipe', 'user')
    search_fields = ('user__username', 'recipe__name')
    list_filter = ('user__username', 'recipe__name')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'recipe', 'user')
    search_fields = ('user__username', 'recipe__name')
    list_filter = ('user__username', 'recipe__name')
