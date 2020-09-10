# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calo', '0003_food_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.CharField(max_length=200, choices=[(b'little/no exercise', b'little/no exercise'), (b'3/week', b'3/week'), (b'4/week', b'4/week'), (b'5/week', b'5/week'), (b'Daily', b'Daily'), (b'Daily(intense)or daily twice', b'Daily(intence)or daily twice'), (b'Daily exercise + physical job', b'Daily exercise + physical job')])),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='food_qty',
            old_name='qauantity',
            new_name='quantity',
        ),
    ]
