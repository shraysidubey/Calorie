# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0005_activity_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food_qty',
            old_name='quantity',
            new_name='calories',
        ),
    ]
