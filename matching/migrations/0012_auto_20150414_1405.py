# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0011_auto_20150414_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='working_hours',
            field=models.ManyToManyField(to='matching.WorkingHours', blank=True),
        ),
    ]
