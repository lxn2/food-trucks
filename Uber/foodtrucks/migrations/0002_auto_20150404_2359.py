# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtrucks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtrucks',
            name='address',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodtrucks',
            name='name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
