# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpss', '0003_auto_20151015_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
