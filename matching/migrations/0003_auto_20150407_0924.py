# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0002_agent_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('fb', models.URLField()),
                ('twitter', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('website', models.URLField(max_length=150)),
                ('price_range', models.CharField(max_length=5)),
                ('rating', models.FloatField(default=0)),
                ('facebook', models.URLField()),
                ('facebook_likes', models.IntegerField(default=0)),
                ('facebook_acivity', models.CharField(max_length=200)),
                ('twitter', models.URLField()),
                ('twitter_followers', models.IntegerField(default=0)),
                ('twitter_tweets', models.IntegerField(default=0)),
                ('instagram', models.URLField()),
                ('instagram_followers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mon', models.CharField(help_text=b'Monday', max_length=20)),
                ('tue', models.CharField(help_text=b'Tuesday', max_length=20)),
                ('wed', models.CharField(help_text=b'Wednesday', max_length=20)),
                ('thu', models.CharField(help_text=b'Thursday', max_length=20)),
                ('fri', models.CharField(help_text=b'Friday', max_length=20)),
                ('sat', models.CharField(help_text=b'Saturday', max_length=20)),
                ('sun', models.CharField(help_text=b'Sunday', max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='contact',
            new_name='company',
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('venue_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='matching.Venue')),
                ('rooms', models.IntegerField(default=1)),
                ('bathrooms', models.IntegerField(default=1)),
                ('beds', models.IntegerField(default=1)),
                ('pool', models.BooleanField(default=False)),
                ('airbnb', models.URLField(max_length=100)),
            ],
            bases=('matching.venue',),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('venue_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='matching.Venue')),
            ],
            bases=('matching.venue',),
        ),
        migrations.CreateModel(
            name='ReCa',
            fields=[
                ('venue_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='matching.Venue')),
                ('type_of_venue', models.CharField(max_length=20)),
                ('cousine_style', models.CharField(max_length=200)),
                ('foods', models.TextField()),
                ('drinks', models.TextField()),
            ],
            bases=('matching.venue',),
        ),
        migrations.AddField(
            model_name='venue',
            name='beach',
            field=models.ForeignKey(related_name='venues', blank=True, to='matching.Beach'),
        ),
        migrations.AddField(
            model_name='venue',
            name='contacts',
            field=models.ManyToManyField(to='matching.Contact'),
        ),
        migrations.AddField(
            model_name='venue',
            name='working_hours',
            field=models.OneToOneField(to='matching.WorkingHours'),
        ),
    ]
