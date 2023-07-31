# Generated by Django 4.1.7 on 2023-07-30 20:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berries',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='berries',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Ягода'),
        ),
        migrations.AlterField(
            model_name='decors',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='decors',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Декор'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Форма торта'),
        ),
        migrations.AlterField(
            model_name='sizes',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='sizes',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Размер торта'),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Топпинг'),
        ),
    ]