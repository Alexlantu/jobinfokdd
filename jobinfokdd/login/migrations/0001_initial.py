# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('LoginID', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=25)),
                ('UserID', models.CharField(max_length=12)),
            ],
        ),
    ]
