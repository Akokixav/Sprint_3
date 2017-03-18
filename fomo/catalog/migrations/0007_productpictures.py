# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20170220_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdir', models.TextField(blank=True, null=True)),
                ('alttext', models.TextField(blank=True, null=True)),
                ('minetype', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
    ]
