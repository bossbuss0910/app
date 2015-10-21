# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='user1id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='user2id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
