# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(max_digits=5, decimal_places=2)),
                ('longitude', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='gps',
            field=models.ForeignKey(to='gpss.Gps'),
        ),
    ]
