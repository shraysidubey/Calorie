# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0006_auto_20200901_0648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='user',
        ),
        migrations.AlterField(
            model_name='food_qty',
            name='user',
            field=models.ForeignKey(to='calo.UserProfile'),
        ),
    ]
