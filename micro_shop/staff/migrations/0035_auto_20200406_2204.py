# Generated by Django 2.2.10 on 2020-04-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0034_auto_20200111_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avito',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='youla',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True, help_text='Оставьте поле пустым, чтобы не отображать ссылку в футере.', verbose_name='профиль Facebook'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram',
            field=models.URLField(blank=True, help_text='Оставьте поле пустым, чтобы не отображать ссылку в футере.', verbose_name='профиль Instagram'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(blank=True, help_text='Оставьте поле пустым, чтобы не отображать ссылку в футере.', verbose_name='профиль Twitter'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='vk',
            field=models.URLField(blank=True, help_text='Оставьте поле пустым, чтобы не отображать ссылку в футере.', verbose_name='профиль VK'),
        ),
    ]
