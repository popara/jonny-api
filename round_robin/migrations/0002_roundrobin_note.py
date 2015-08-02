# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('round_robin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roundrobin',
            name='note',
            field=models.CharField(default='Hello', max_length=20),
            preserve_default=False,
        ),
    ]
