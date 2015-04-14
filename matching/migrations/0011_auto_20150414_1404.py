# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0010_auto_20150414_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='airbnb',
            field=models.URLField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='working_hours',
            field=models.ManyToManyField(to='matching.WorkingHours', null=True, blank=True),
        ),
    ]
