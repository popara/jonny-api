# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0007_auto_20150407_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='google_place_id',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
