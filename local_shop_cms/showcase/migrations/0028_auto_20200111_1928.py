# Generated by Django 2.2.9 on 2020-01-11 19:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0027_auto_20200109_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sort_position',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(help_text='Длинна описания должна быть от 100 до 500 символов.', max_length=500, validators=[django.core.validators.MinLengthValidator(100)], verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='item_images', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(help_text='Длинна названия не может превышать 20 символов.', max_length=20, verbose_name='название'),
        ),
    ]