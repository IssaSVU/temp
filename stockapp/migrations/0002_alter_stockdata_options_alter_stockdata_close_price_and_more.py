# Generated by Django 5.0.3 on 2024-03-22 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockdata',
            options={'verbose_name_plural': 'Stocks Data'},
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='close_price',
            field=models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(0, 'Price must be greater than zero')]),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='open_price',
            field=models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(0, 'Price must be greater than zero')]),
        ),
    ]
