# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0004_auto_20150407_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='beach',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='beach',
            name='lng',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='venue',
            name='contacts',
            field=models.ManyToManyField(to='matching.Contact', blank=True),
        ),
    ]
