# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0009_auto_20150408_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='price_range',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
