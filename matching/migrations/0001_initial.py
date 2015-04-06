# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('website', models.URLField()),
                ('company_phone', models.CharField(max_length=200)),
                ('personal_phone', models.CharField(max_length=200)),
                ('skype', models.CharField(max_length=50)),
                ('whatsapp', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('facebook_page', models.URLField()),
                ('facebook_likes', models.IntegerField()),
                ('facebook_posts', models.IntegerField()),
                ('facebook_last_post', models.DateField()),
                ('twitter', models.URLField()),
                ('twitter_tweets', models.IntegerField()),
                ('twitter_followers', models.IntegerField()),
                ('linkedin', models.URLField()),
                ('fees', models.IntegerField()),
                ('english', models.BooleanField(default=False)),
                ('spanish', models.BooleanField(default=False)),
                ('dutch', models.BooleanField(default=False)),
                ('german', models.BooleanField(default=False)),
                ('russian', models.BooleanField(default=False)),
                ('french', models.BooleanField(default=False)),
                ('italian', models.BooleanField(default=False)),
                ('portuguese', models.BooleanField(default=False)),
                ('arabic', models.BooleanField(default=False)),
                ('SEO', models.CharField(max_length=10)),
                ('SEM', models.CharField(max_length=10)),
                ('hq', models.CharField(max_length=100)),
                ('local_office', models.TextField()),
                ('other_office', models.TextField()),
                ('services', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
