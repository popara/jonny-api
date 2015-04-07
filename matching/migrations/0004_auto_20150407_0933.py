# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0003_auto_20150407_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beach',
            name='type',
            field=models.CharField(max_length=10, choices=[(b'sandy', b'Sandy'), (b'rocky', b'Rocky'), (b'concrete', b'Concrete'), (b'misc', b'Mixed')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fb',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='reca',
            name='drinks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='reca',
            name='foods',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='contacts',
            field=models.ManyToManyField(to='matching.Contact', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='facebook_acivity',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='facebook_likes',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='instagram_followers',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='price_range',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='rating',
            field=models.FloatField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='twitter_followers',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='twitter_tweets',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='website',
            field=models.URLField(max_length=150, blank=True),
        ),
        migrations.RemoveField(
            model_name='venue',
            name='working_hours',
        ),
        migrations.AddField(
            model_name='venue',
            name='working_hours',
            field=models.ManyToManyField(to='matching.WorkingHours'),
        ),
    ]
