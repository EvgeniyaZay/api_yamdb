# Generated by Django 2.2.16 on 2022-08-29 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20220829_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(verbose_name='Год издания'),
        ),
    ]
