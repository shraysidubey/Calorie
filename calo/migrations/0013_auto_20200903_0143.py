# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0012_auto_20200903_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='burn_calorie',
            new_name='calories_burned',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='date',
        ),
        migrations.AddField(
            model_name='activity',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity',
            field=models.TextField(max_length=200),
        ),
    ]
