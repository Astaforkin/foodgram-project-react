from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    """Модель ингредиентов для рецепта"""
    name = models.CharField(verbose_name='Название ингредиента',
                            max_length=200)
    unit = models.CharField(verbose_name='Единица измерения',
                                         max_length=200)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']


class Tag(models.Model):
    """Модель тегов для рецепта"""
    name = models.CharField(verbose_name='Название тега',
                            max_length=200,
                            unique=True)
    color = models.CharField(verbose_name='Цвет тега',
                             max_length=200,
                             unique=True)
    slug = models.SlugField(verbose_name='Слаг тега',
                            max_length=200,
                            unique=True)

    class Meta:
        verbose_name = ' Тег',
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецептов"""
    name = models.CharField(verbose_name='Название блюда', max_length=255)
    text = models.TextField(verbose_name='Текст рецепта')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Автор',
        related_name='recipes'
    )
    time_to_prepare = models.IntegerField(verbose_name='Время приготовления',
                                          default=0)
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингридиенты для приготовления блюда',
        related_name='recipes'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег для рецепта',
        related_name='recipes'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']

    def __str__(self) -> str:
        return self.name


class IngredientAmount(models.Model):
    """Привязка количества ингредиента к рецепту"""
    amount = models.IntegerField(
        verbose_name='Количество ингредиента в рецепте'
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='К какому рецепту относится',
        related_name='ingredient_amount',
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='К какому ингредиенту относится',
        related_name='ingredient_amount',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        ordering = ['recipe']
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_ingredient_in_recipe',
            )
        ]

    def __str__(self) -> str:
        return f'{self.recipe} - {self.ingredient} - {self.amount}'