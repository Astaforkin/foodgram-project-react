import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('static/data/ingredients.csv', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    Ingredient.objects.get_or_create(
                        name=row[0],
                        measurement_unit=row[1]
                    )
            except Exception as error:
                print(row)
                print(
                        f'Ошибка записи в таблицу модели '
                        f'{cf["model"].__name__}, '
                        f'{str(error)}')
