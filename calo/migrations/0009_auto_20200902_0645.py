# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0008_food_qty_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food_qty',
            old_name='date',
            new_name='date_added',
        ),
    ]
