# Generated by Django 2.2.16 on 2022-08-28 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20220828_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Reviews', verbose_name='Ревью'),
        ),
    ]