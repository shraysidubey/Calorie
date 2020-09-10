# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0009_auto_20200902_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food_qty',
            name='date_added',
        ),
        migrations.AddField(
            model_name='food_qty',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
