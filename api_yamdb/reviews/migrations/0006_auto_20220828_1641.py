# Generated by Django 2.2.19 on 2022-08-28 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220828_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': ('Категория',), 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': ('Жанр',), 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={},
        ),
        migrations.AlterModelOptions(
            name='titlegenre',
            options={},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]