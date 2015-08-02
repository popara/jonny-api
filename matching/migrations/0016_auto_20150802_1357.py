# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0015_accomodation_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accomodation',
            name='venue_ptr',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='venue_ptr',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.RemoveField(
            model_name='reca',
            name='venue_ptr',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='beach',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='working_hours',
        ),
        migrations.DeleteModel(
            name='Accomodation',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='Beach',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='ReCa',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
        migrations.DeleteModel(
            name='WorkingHours',
        ),
    ]
