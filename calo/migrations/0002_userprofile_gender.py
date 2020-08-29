# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=datetime.date(2020, 8, 28), max_length=11, choices=[(b'female', b'Female'), (b'male', b'male')]),
            preserve_default=False,
        ),
    ]
