# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0013_auto_20200903_0143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity',
            new_name='exercise',
        ),
    ]
