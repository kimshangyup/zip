# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('text1', models.CharField(max_length=200)),
                ('text2', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
