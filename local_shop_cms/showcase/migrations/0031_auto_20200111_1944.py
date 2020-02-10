# Generated by Django 2.2.9 on 2020-01-11 19:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0030_auto_20200111_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sort_position',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='Позиция на главной'),
        ),
    ]