# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0013_auto_20150422_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='ready',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
