# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0012_auto_20150414_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='internal_note',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='venue',
            name='internal_rating',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
