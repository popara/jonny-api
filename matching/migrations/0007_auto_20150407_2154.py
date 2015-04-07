# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0006_auto_20150407_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='beach',
            field=models.ForeignKey(related_name='venues', blank=True, to='matching.Beach', null=True),
        ),
    ]
