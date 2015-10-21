# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpss', '0002_auto_20151015_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='gps',
        ),
        migrations.RemoveField(
            model_name='gps',
            name='id',
        ),
        migrations.AlterField(
            model_name='gps',
            name='u_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
