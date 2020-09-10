# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calo', '0011_auto_20200902_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='burn_calorie',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(default=187, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
