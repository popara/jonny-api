# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0005_auto_20150407_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='google_place_id',
            field=models.CharField(default='UnoDueTre', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='venue',
            name='lng',
            field=models.FloatField(default=0),
        ),
    ]
