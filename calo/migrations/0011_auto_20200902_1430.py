# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0010_auto_20200902_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food_qty',
            old_name='release_date',
            new_name='date_added',
        ),
    ]
