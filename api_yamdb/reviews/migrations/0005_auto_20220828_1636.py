# Generated by Django 2.2.19 on 2022-08-28 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220828_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['name'], 'verbose_name': ('Категория',), 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ['name'], 'verbose_name': ('Жанр',), 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['name'], 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.AlterModelOptions(
            name='titlegenre',
            options={'verbose_name': 'Произведение и жанр', 'verbose_name_plural': 'Произведения и жанры'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
    ]
