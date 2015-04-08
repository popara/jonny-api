# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0008_auto_20150407_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beach',
            name='address',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
