# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTrucks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('fooditems', models.TextField(max_length=600, null=True, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=50, decimal_places=30, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=50, decimal_places=30, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food', models.IntegerField(default=20, choices=[(1, b'burger'), (2, b'hot dog'), (3, b'sandwich'), (4, b'indian'), (5, b'korean'), (6, b'vietnamese'), (7, b'mexican'), (8, b'chinese'), (9, b'pizza'), (10, b'bbq'), (11, b'cold truck'), (12, b'taco'), (13, b'italian'), (14, b'filipino'), (15, b'seafood'), (16, b'asian'), (17, b'peruvian'), (18, b'gyro'), (19, b'coffee'), (20, b'other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='foodtrucks',
            name='foodtypes',
            field=models.ManyToManyField(related_name='trucks', null=True, to='foodtrucks.FoodTypes', blank=True),
            preserve_default=True,
        ),
    ]
