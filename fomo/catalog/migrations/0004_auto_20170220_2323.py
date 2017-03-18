# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bulkproduct_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkproduct',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bulkproduct',
            name='reorder_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bulkproduct',
            name='reorder_trigger',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bulkproduct',
            name='serial_number',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='rentalproduct',
            name='serial_number',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='uniqueproduct',
            name='serial_number',
            field=models.TextField(default=0),
        ),
    ]