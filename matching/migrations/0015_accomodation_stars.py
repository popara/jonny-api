# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0014_venue_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodation',
            name='stars',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
