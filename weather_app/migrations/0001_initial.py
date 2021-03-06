# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherNotifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='Email', blank=True)),
                ('location', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
