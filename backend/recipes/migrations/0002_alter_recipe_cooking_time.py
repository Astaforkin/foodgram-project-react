# Generated by Django 3.2.3 on 2023-08-22 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Минимальное значение - 1')], verbose_name='Время приготовления'),
        ),
    ]
