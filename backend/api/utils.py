from recipes.models import IngredientAmount


def ingredient_amount_set(recipe, ingredients_data):
    """Создает связи рецепта с количеством ингредиента."""
    ingredients = []
    for ingredient_data in ingredients_data:
        id = ingredient_data.get('id')
        amount = ingredient_data.get('amount')
        ingredients.append(IngredientAmount(
            recipe=recipe, ingredient_id=id, amount=amount
        ))
    IngredientAmount.objects.bulk_create(
        ingredients
    )
