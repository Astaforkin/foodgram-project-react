from csv import DictReader

from django.core.management.base import BaseCommand
from recipes.models import Ingredient

csv_files = [
    {'model': Ingredient, 'filename': 'ingredients.csv',
     'fieldnames': ['name', 'measurement_unit']},
]


class Command(BaseCommand):
    """Загружает ингредиенты из файла csv."""

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Путь к csv файлу')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = DictReader(file)
            for row in reader:
                ingredient, created = (
                    Ingredient.objects.update_or_create(
                        name=row['name'],
                        measurement_unit=row['measurement_unit']
                    )
                )
