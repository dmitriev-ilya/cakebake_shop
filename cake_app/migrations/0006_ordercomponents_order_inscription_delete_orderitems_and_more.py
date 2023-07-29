# Generated by Django 4.1.7 on 2023-07-29 07:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_app', '0005_remove_orderitems_catalog_cake_ordercatalogcakes'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='количество')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена в заказе')),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='cake_app.component', verbose_name='компонент торта')),
            ],
            options={
                'verbose_name': 'состав заказа',
                'verbose_name_plural': 'состав заказа',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='inscription',
            field=models.TextField(blank=True, verbose_name='надпись на торт'),
        ),
        migrations.DeleteModel(
            name='OrderItems',
        ),
        migrations.AddField(
            model_name='ordercomponents',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cake_app.order', verbose_name='заказ'),
        ),
    ]
