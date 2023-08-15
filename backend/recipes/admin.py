from django.contrib import admin

from .models import Follow, Ingredient, IngredientAmount, Recipe, Tag, User


class IngredientAdmin(admin.ModelAdmin):
    # list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('amount', 'recipe', 'ingredient')
    search_fields = ('recipe__name', 'ingredient__name')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'time_to_prepare')
    search_fields = ('name', 'author__username', 'tags__name')
    list_filter = ('name', 'author__username', 'tags__name')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user', 'following')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Follow, FollowAdmin)
